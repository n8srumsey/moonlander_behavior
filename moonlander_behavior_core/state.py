from ArucoMarkerTracking import ArucoMultiTracker
from moonlander import Drone

class State:
    def __init__(self, drone: Drone, ArucoTracker:ArucoMultiTracker=None) -> None:
        self.drone = drone
        self.tracker:ArucoMultiTracker= ArucoTracker
    
        self.armed = drone.armed
        self.drone_status = drone.status
        self.tracker_status = self.tracker.track()

    def update_state(self):
        self.tracker_status = self.tracker.track()
