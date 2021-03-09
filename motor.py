import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.robot = None
        self.motorValues = None
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.phaseOffset = c.phaseOffsetBackLeg
        self.prepareToAct()

    def prepareToAct(self):
        if self.jointName == "Torso_FrontLeg":
            self.frequency = self.frequency / 2
        else:
            pass
        self.motorValues = self.amplitude * numpy.sin(self.frequency * (numpy.linspace(-numpy.math.pi, numpy.math.pi, 1000)) + self.phaseOffset)
#.21014, .38419
    def setValue(self, t, robot):
        self.robot = robot
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=50)

    def saveValues(self):
        numpy.save("data/" + self.jointName + "MotorValues.npy", self.motorValues)
