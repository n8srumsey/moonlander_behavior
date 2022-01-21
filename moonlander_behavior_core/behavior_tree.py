from moonlander import Drone

from .behavior import Behavior
from .condition import Condition
from .state import State


class Node:
    def __init__(self, content, left=None, right=None) -> None:
        self.content = content
        self.left_t = left
        self.right_f = right

    def propogate(self, state):
        if issubclass(type(self.content), Behavior):
            self.content.action(state)
        elif issubclass(type(self.content), Condition):
            check = self.content.check()
            if check:
                self.left_t.propogate(state)
            else:
                self.right_f.propogate(state)
        

class BinaryBehaviorTree:
    def __init__(self, drone: Drone, state: State) -> None:
        self.drone = drone
        self.state = state
        self.root = None
    
    def propogate(self):
        self.state.update_state()
        self.root.propogate(self.state)
