from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time as t
#from simulate import directOrGUI

class SIMULATION:
    def __init__(self, directOrGUI):

        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # simulate earth gravity
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for x in range (0, 1000):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
            # # log for sensor values
            #t.sleep(1/30)

    def Get_Fitness(self):
        self.robot.Get_Fitness()


def __del__(self):
    p.disconnect()
