from xmlrpc.client import Boolean
from ArucoMarkerTracking import ArucoMultiTracker


class State:
    def __init__(self, drone:Drone, ArucoTracker:ArucoMultiTracker=None) -> None:
        self.drone:Drone = drone
        self.tracker:ArucoMultiTracker= ArucoTracker
    
        self.armed:Boolean = drone.armed
        self.drone_status = drone.status
        self.tracker_status = self.tracker.track()

    def update_state(self):
        self.tracker_status = self.tracker.track()
