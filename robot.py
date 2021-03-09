import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        ROBOT.prepareToSense(self)
        ROBOT.prepareToAct(self)

    def prepareToSense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self, t):
        for i in self.sensors:
            self.sensors[i].getValue(t)

    def prepareToAct(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self, t):
        for i in self.motors:
            self.motors[i].setValue(t, self.robot)
