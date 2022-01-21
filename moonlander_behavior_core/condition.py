from .state import State

class Condition:
    def __init__(self, condition_func: function) -> None:
        self._condition_function = condition_func

    def check(self, state: State):
        return self._condition_function(state)
    
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