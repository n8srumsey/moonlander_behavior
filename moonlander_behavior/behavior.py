from moonlander import Drone, meters_to_deg

from .behavior_tree import Node
from .state import State

class Behavior(Node):
    def __init__(self, action: function, priority: int) -> None:
        super().__init__(action)
        self.priority = priority
        
    def action(self, state: State) -> None:
        self.func(state.drone, state)
        
    def propogate(self, _):
        return self
    


""" Common Behaviors """
class GoTo(Behavior):
    def __init__(self, meters_x: float, meters_y: float) -> None:
        async def goto(drone: Drone, state: State):
            await drone.goto_position_from_home(meters_to_deg(meters_x), meters_to_deg(meters_y))
        super().__init__(goto)

class Arm(Behavior):
    def __init__(self) -> None:
        async def arm_drone(drone: Drone, state: State):
            await drone.arm()
        super().__init__(arm_drone)
