from .state import State
from moonlander import Drone, meters_to_deg

class Behavior:
    def __init__(self, behavior_func: function) -> None:
        self._behavior = behavior_func

    def action(self, state: State) -> None:
        self._behavior(state.drone, state)


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