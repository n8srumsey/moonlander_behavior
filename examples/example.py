from ArucoMarkerTracking import ArucoMultiTracker

from moonlander_behavior.condition import *
from moonlander_behavior.behavior import *
from moonlander_behavior.behavior_tree import *


drone = Drone()
ArucoTracker = ArucoMultiTracker(...)

state = State(drone, ArucoTracker)

behavior_tree = BinaryBehaviorTree(drone, state)

behavior_tree.root = Node(IsArmed(), 
                          left=Node(DetectsAruco(),
                                left=Node(GoTo(10., 10.), 
                                    left=None, 
                                    right=None),
                                right=None), 
                          right=Node(Arm(), 
                                left=None, 
                                right=None))
