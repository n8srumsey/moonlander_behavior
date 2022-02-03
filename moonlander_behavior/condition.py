from .behavior_tree import Node
from .state import State

class Condition(Node):
    def __init__(self, func: function) -> None:
        super().__init__(func)

    def check(self, state: State):
        return self.func(state)
    
    def propogate(self, state):
        if self.check(state):
            return self.true.propogate(state)
        return self.false.propogate(state)
    
"""Common Conditions"""
class DetectsAruco(Condition):
    def __init__(self) -> None:
        def detects_aruco_marker(state: State):
            return state.tracker_status[0]
        super().__init__(detects_aruco_marker)
        
class IsArmed(Condition):
    def __init__(self) -> None:
        def is_armed(state: State):
            return state.armed
        super().__init__(is_armed)       