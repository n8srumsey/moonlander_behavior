from .state import State

class Condition:
    def __init__(self, condition_func: function) -> None:
        self._condition_function = condition_func

    def check(self, state: State):
        return self._condition_function(state)