import pybullet as p
import pybullet_data
import time as t
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        # connect to service
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # instantiate world and robot
        self.world = WORLD()
        self.robot = ROBOT()

        # simulate gravity
        p.setGravity(0, 0, -9.8)

    def run(self):
        # loop through to run simulation
        for i in range(0, 1000):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.act(i)
            t.sleep(1 / 10)

    def __del__(self):
        p.disconnect()
