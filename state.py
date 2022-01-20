from ArucoMarkerTracking import ArucoMultiTracker


class State:
    def __init__(self, drone, ArucoTracker:ArucoMultiTracker=None) -> None:
        self.drone = drone
        self.tracker = ArucoTracker
    
        self.armed = drone.armed


    def get_state(self):
        if self.tracker is None:
            return self.drone
        return self.drone, self.tracker.track()
