import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.myID = solutionID
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)
        os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robot)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLink0 = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLink0[0]
        #f = open("fitness"+ str(solutionID) + ".txt", 'w')
        f = open("tmp" + str(solutionID) + ".txt", 'w')
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" + str(solutionID) + ".txt")
        #exit()
