
import copy
import heapq
import math
import numpy as np

class TreeNode:
    def __init__(self, parent, game_state, p, d, action):
        self._game_state = game_state
        self._p = p
        self._d = d
        self._action = action
        self._parent = parent
        self._probabilitiy_distribution_a = None
    
    def __eq__(self, other):
        """
        Verify if two tree nodes are identical by verifying the 
        game state in the nodes. 
        """
        return self._game_state == other._game_state
    
    def __lt__(self, other):
        """
        Function less-than used by the heap
        """
        return self._levin_cost < other._levin_cost    
    
    def __hash__(self):
        """
        Hash function used in the closed list
        """
        return self._game_state.__hash__()
    
    def set_probability_distribution_actions(self, d):
        self._probabilitiy_distribution_a = d
        
    def get_probability_distribution_actions(self):
        return self._probabilitiy_distribution_a
    
    def set_levin_cost(self, c):
        self._levin_cost = c
    
    def get_p(self):
        """
        Returns the pi cost of a node
        """
        return self._p
    
    def get_depth(self):
        """
        Returns the pi cost of a node
        """
        return self._d
    
    def get_game_state(self):
        """
        Returns the game state represented by the node
        """
        return self._game_state
    
    def get_parent(self):
        """
        Returns the parent of the node
        """
        return self._parent
    
    def get_action(self):
        """
        Returns the action taken to reach node stored in the node
        """
        return self._action
    def get_levin_cost(self):
        return self._levin_cost  

class Trajectory():
    def __init__(self, states, actions):
        self._states = states
        self._actions = actions
        
    def get_states(self):
        return self._states
    
    def get_actions(self):
        return self._actions
    
    def length(self):
        return len(self._states)
    
class LevinTS():
            
    def recover_path(self, tree_node):
        states = []
        actions = []
        
        state = tree_node.get_parent()
        action = tree_node.get_action()
        
        while not state.get_parent() is None:
            states.append(state.get_game_state())
            actions.append(action)
            
            action = state.get_action()
            state = state.get_parent()
            
        states.append(state.get_game_state())
        actions.append(action)
        
        return Trajectory(states, actions)  

    def get_levin_cost(self, node):
        """
     Computes the Levin cost of a node using the formula:
     Levin Cost = depth / probability
     """
        depth = node.get_depth()
        log_depth = np.log(depth + 1)  
        log_probability = node.get_p()  # Probability is already in log-space
        return log_depth - log_probability  # Log space prevents numerical issues

        
    def search(self, state, model, budget):
     """
     Implements Levin Tree Search (LevinTS) to find a solution to the puzzle.

     Parameters:
       state (WitnessState): Initial state of the puzzle.
       model: The policy model used for action probabilities.
       budget (int): Maximum number of node expansions.
     Returns:
       tuple: (solution_cost, num_expansions, solution_path)
     """
     # Priority queue for best-first search (Levin cost as priority)
     open_list = []
    
     # Closed set to avoid expanding the same state multiple times
     closed_set = set()

    # Root node initialization
     root_node = TreeNode(None, state, 0, 0, -1)
     heapq.heappush(open_list, root_node)
   
     expansions = 0  # Counter for expanded nodes

     while open_list and expansions < budget:
        # Get the node with the lowest Levin cost
        current_node = heapq.heappop(open_list)

        # Check if the current state is a solution
        if current_node.get_game_state().is_solution():
            return current_node.get_levin_cost(), expansions, self.recover_path(current_node)

        # Mark state as visited
        game_state = current_node.get_game_state()
        state_tuple = getattr(game_state, "to_tuple", lambda: hash(game_state))()  # Use to_tuple() if available
        if state_tuple in closed_set:
            continue
        closed_set.add(state_tuple)

        # Expand the node
        actions = game_state.successors_parent_pruning(current_node.get_action())
        probability_distribution = model.get_probabilities(game_state.get_pattern())
        probability_distribution_log = np.log(probability_distribution)

        for action in actions:
            child_state = copy.deepcopy(game_state)
            child_state.apply_action(action)

            # Compute new depth and log probability
            new_depth = current_node.get_depth() + 1
            new_prob = current_node.get_p() + probability_distribution_log[action]

            # Create child node
            child_node = TreeNode(current_node, child_state, new_prob, new_depth, action)
            child_node.set_probability_distribution_actions(probability_distribution_log)

            # Compute and set Levin cost
            levin_cost = self.get_levin_cost(child_node)
            child_node.set_levin_cost(levin_cost)

            heapq.heappush(open_list, child_node)

        expansions += 1

    # If budget is reached without a solution, return failure case
     return -1, expansions, None
