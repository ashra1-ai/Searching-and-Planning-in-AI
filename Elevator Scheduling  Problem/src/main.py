from ortools.sat.python import cp_model
import json
import argparse
import time
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple
from enum import IntEnum
import sys


class Action(IntEnum):
    UP = 0
    DOWN = 1
    BOARD = 2
    DEPART = 3
    WAIT = 4


class Passenger:
    def __init__(self, passenger_id: int, origin: int, destination: int):
        self.id = passenger_id
        self.origin = origin
        self.destination = destination


class ElevatorScheduler:
    def __init__(self, num_floors: int, passengers: List[Passenger], horizon: int):
        self.model = cp_model.CpModel()
        self.num_floors = num_floors
        self.horizon = horizon
        self.passengers = passengers
       
        # Variables
        self.floor = [self.model.NewIntVar(0, num_floors-1, f"floor_{t}") for t in range(horizon)]
        self.actions = [self.model.NewIntVar(0, len(Action)-1, f"action_{t}") for t in range(horizon)]
        self.passenger_status = [
            [self.model.NewIntVar(0, 2, f"pass_{p.id}_{t}") for t in range(horizon)]
            for p in passengers
        ]
       
        self._add_basic_constraints()


    def _add_basic_constraints(self):
        # Initial conditions
        self.model.Add(self.floor[0] == 0)
        for p_idx in range(len(self.passengers)):
            self.model.Add(self.passenger_status[p_idx][0] == 0)
       
        # Goal conditions
        for p_idx in range(len(self.passengers)):
            self.model.Add(self.passenger_status[p_idx][-1] == 2)
       
        for t in range(1, self.horizon):
            self._add_time_step_constraints(t)


    def _add_time_step_constraints(self, t: int):
        prev_floor = self.floor[t-1]
        curr_floor = self.floor[t]
        action = self.actions[t-1]


        # Movement constraints
        self.model.Add(curr_floor <= prev_floor + 1)
        self.model.Add(curr_floor >= prev_floor - 1)
       
        # Action constraints
        move_up = self.model.NewBoolVar(f"up_{t}")
        self.model.Add(action == Action.UP).OnlyEnforceIf(move_up)
        self.model.Add(curr_floor == prev_floor + 1).OnlyEnforceIf(move_up)


        move_down = self.model.NewBoolVar(f"down_{t}")
        self.model.Add(action == Action.DOWN).OnlyEnforceIf(move_down)
        self.model.Add(curr_floor == prev_floor - 1).OnlyEnforceIf(move_down)


        stay = self.model.NewBoolVar(f"stay_{t}")
        self.model.Add(action == Action.WAIT).OnlyEnforceIf(stay)
        self.model.Add(curr_floor == prev_floor).OnlyEnforceIf(stay)


        # Exactly one action per time step
        self.model.AddExactlyOne([move_up, move_down, stay])


        # Passenger constraints
        for p_idx, passenger in enumerate(self.passengers):
            prev_status = self.passenger_status[p_idx][t-1]
            curr_status = self.passenger_status[p_idx][t]
           
            # State progression
            self.model.Add(curr_status >= prev_status)
            self.model.Add(curr_status <= prev_status + 1)


            # Boarding constraints
            boarding = self.model.NewBoolVar(f"board_{p_idx}_{t}")
            self.model.Add(prev_floor == passenger.origin).OnlyEnforceIf(boarding)
            self.model.Add(prev_status == 0).OnlyEnforceIf(boarding)
            self.model.Add(action == Action.BOARD).OnlyEnforceIf(boarding)
            self.model.Add(curr_status == 1).OnlyEnforceIf(boarding)


            # Departing constraints
            departing = self.model.NewBoolVar(f"depart_{p_idx}_{t}")
            self.model.Add(prev_floor == passenger.destination).OnlyEnforceIf(departing)
            self.model.Add(prev_status == 1).OnlyEnforceIf(departing)
            self.model.Add(action == Action.DEPART).OnlyEnforceIf(departing)
            self.model.Add(curr_status == 2).OnlyEnforceIf(departing)


            # Status persistence
            no_change = self.model.NewBoolVar(f"no_change_{p_idx}_{t}")
            self.model.AddBoolAnd([boarding.Not(), departing.Not()]).OnlyEnforceIf(no_change)
            self.model.Add(curr_status == prev_status).OnlyEnforceIf(no_change)


    def solve(self) -> float:
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 30.0
        start_time = time.time()
        status = solver.Solve(self.model)
        runtime = time.time() - start_time
        return runtime if status in [cp_model.OPTIMAL, cp_model.FEASIBLE] else float('inf')


class GreedyScheduler(ElevatorScheduler):
    def solve(self) -> float:
        solver = cp_model.CpSolver()
        solver.parameters.search_branching = cp_model.FIXED_SEARCH
        solver.parameters.cp_model_presolve = False
        solver.parameters.linearization_level = 0
        solver.parameters.cp_model_probing_level = 0
        start_time = time.time()
        status = solver.Solve(self.model)
        runtime = time.time() - start_time
        return runtime if status in [cp_model.OPTIMAL, cp_model.FEASIBLE] else float('inf')


class OptimizedScheduler(ElevatorScheduler):
    def _add_time_step_constraints(self, t: int):
        super()._add_time_step_constraints(t)
        if t > 0:
            # Prevent immediate direction reversal
            prev_up = self.model.NewBoolVar(f'prev_up_{t}')
            self.model.Add(self.actions[t-1] == Action.UP).OnlyEnforceIf(prev_up)
            curr_down = self.model.NewBoolVar(f'curr_down_{t}')
            self.model.Add(self.actions[t] == Action.DOWN).OnlyEnforceIf(curr_down)
            self.model.AddImplication(prev_up, curr_down.Not())


            prev_down = self.model.NewBoolVar(f'prev_down_{t}')
            self.model.Add(self.actions[t-1] == Action.DOWN).OnlyEnforceIf(prev_down)
            curr_up = self.model.NewBoolVar(f'curr_up_{t}')
            self.model.Add(self.actions[t] == Action.UP).OnlyEnforceIf(curr_up)
            self.model.AddImplication(prev_down, curr_up.Not())


def load_input_file(input_file: str) -> Tuple[int, List[Passenger], int]:
    try:
        with open(input_file) as f:
            data = json.load(f)
       
        passengers = [Passenger(p['id'], p['origin'], p['destination'])
                     for p in data['passengers']]
       
        # Validate input
        num_floors = data['num_floors']
        for p in passengers:
            if not (0 <= p.origin < num_floors and 0 <= p.destination < num_floors):
                raise ValueError(f"Passenger {p.id} has invalid floor (must be 0-{num_floors-1})")
            if p.origin == p.destination:
                raise ValueError(f"Passenger {p.id} has same origin and destination")
       
        return num_floors, passengers, data['plan_horizon']
   
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in input file '{input_file}'", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing required field {e} in input file", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def plot_runtime_comparison(runtimes: Dict[str, float]):
    names = list(runtimes.keys())
    values = [runtimes[name] for name in names]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
   
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, values, color=colors)
    plt.title('Elevator Scheduling Runtime Comparison')
    plt.ylabel('Runtime (seconds)')
   
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}', ha='center', va='bottom')
   
    plt.tight_layout()
    plt.savefig('runtime_comparison.png', dpi=300)
    plt.close()
    print("\nRuntime comparison saved to 'runtime_comparison.png'")


def compare_schedulers(input_file: str) -> None:
    print(f"\n{' Elevator Scheduling Runtime Comparison ':=^80}")
   
    try:
        num_floors, passengers, horizon = load_input_file(input_file)
    except Exception as e:
        print(f"Failed to load input file: {e}", file=sys.stderr)
        return
   
    print(f"\nProblem Configuration:")
    print(f"- Number of Floors: {num_floors}")
    print(f"- Number of Passengers: {len(passengers)}")
    print(f"- Time Horizon: {horizon}")
   
    schedulers = {
        'Basic': ElevatorScheduler,
        'Greedy': GreedyScheduler,
        'Optimized': OptimizedScheduler
    }
   
    runtimes = {}
   
    print("\nMeasuring scheduler runtimes...")
    for name, scheduler_class in schedulers.items():
        print(f"  Running {name} scheduler...", end='', flush=True)
        scheduler = scheduler_class(num_floors, passengers, horizon)
        runtime = scheduler.solve()
        runtimes[name] = runtime
        print(f" completed in {runtime:.3f} seconds")
   
    print("\nRuntime Results:")
    for name, runtime in runtimes.items():
        print(f"{name:<10}: {runtime:.3f} seconds")
   
    plot_runtime_comparison(runtimes)
    print("\n" + "=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare runtime of elevator scheduling algorithms",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input', required=True,
                       help="JSON input file with problem definition")
    args = parser.parse_args()
   
    compare_schedulers(args.input)

