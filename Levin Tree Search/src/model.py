import numpy as np
from levin_tree_search import LevinTS    
from witness import WitnessState
class UniformModel:
    def get_probabilities(self, _):
        return np.ones(4) / 4

class Model:
    def __init__(self):
        self._table = {}
        self._increment = 10

    def get_probabilities(self, pattern):
        if pattern not in self._table:
            self._table[pattern] = np.ones(4)

        return self._table[pattern] / np.sum(self._table[pattern])
    
    def update(self, path, version=2):
     """
     Updates the model based on a given solution trajectory.

     Args:
     - path (Trajectory): The solution path containing states and actions.
     - version (int): Determines whether to update only the regular context (1)
                     or both regular and reversed contexts (2).
     """
     for state, action in zip(path.get_states(), path.get_actions()):
        # Get the regular and reversed context patterns
        regular, reversed = state.get_reversed_pattern()

        # Ensure context entries exist in the table
        if regular not in self._table:
            self._table[regular] = np.ones(4)  # Initialize with uniform counts
        if version == 2 and reversed not in self._table:
            self._table[reversed] = np.ones(4)

        # Update the action count
        self._table[regular][action] += self._increment
        if version == 2:
            self._table[reversed][action] += self._increment  # Update both versions if needed
