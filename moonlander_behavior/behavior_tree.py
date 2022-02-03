from abc import abstractmethod

from moonlander import Drone

from .state import State


class Node:
    def __init__(self, func) -> None:
        self.func:function = func
        self.true:Node = None
        self.false:Node= None
        
    @abstractmethod
    def propogate(self, state):
        pass
        

class BinaryBehaviorTree:
    def __init__(self, drone: Drone, state: State) -> None:
        self.drone = drone
        self.state = state
        self.root = None
    
    def propogate(self):
        self.state.update_state()
        return self.root.propogate(self.state)
