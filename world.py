import pybullet as p

class WORLD:
    def __init__(self):
        # #load floor and world
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
