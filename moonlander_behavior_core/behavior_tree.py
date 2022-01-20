from .behavior import Behavior
from .condition import Condition
from .state import State


class Node:
    def __init__(self, content) -> None:
        self.content = content
        self.left_t = None
        self.right_f = None

    def propogate(self, state):
        if type(self.content) == Behavior:
            self.content.action(state)
        elif type(self.content) == Condition:
            check = self.content.check()
            if check:
                self.left_t.propogate(state)
            else:
                self.right_f.propogate(state)
        

class BinaryBehaviorTree:
    def __init__(self, drone, state: State) -> None:
        self.drone = drone
        self.state = state
        self.root = None
    
    def propogate(self):
        self.state.update_state()
        self.root.propogate(self.state)
