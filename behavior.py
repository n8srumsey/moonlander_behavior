from .state import State

class Behavior:
    def __init__(self, behavior_func: function) -> None:
        self._behavior = behavior_func

    def action(self, state: State) -> None:
        self._behavior(state.drone, state)


""" Common Behaviors """