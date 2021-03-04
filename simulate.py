from simulation import SIMULATION

import pybullet as p
import pybullet_data
import time as t
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c


simulation = SIMULATION()


# #load floor and robot body
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")
#
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate("body.urdf")
#
#
# for i in range (len(c.targetAnglesBackLeg)):
#     c.targetAnglesBackLeg[i] = c.amplitudeBackLeg * numpy.sin(c.frequencyBackLeg * c.targetAnglesBackLeg[i] + c.phaseOffsetBackLeg)
#
#
# for i in range (len(c.targetAnglesFrontLeg)):
#     c.targetAnglesFrontLeg[i] = c.amplitudeFrontLeg * numpy.sin(c.frequencyFrontLeg * c.targetAnglesFrontLeg[i] + c.phaseOffsetFrontLeg)
#
#
# #loop through to run simulation
# for i in range (0, 1000):
#     p.stepSimulation()
#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robot,
#         jointName = "Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.targetAnglesBackLeg[i],
#         maxForce = 20)
#
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robot,
#         jointName = "Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = c.targetAnglesFrontLeg[i],
#         maxForce = 20)
#
#     t.sleep(1/60)
#
# print(c.backLegSensorValues)
# print(c.frontLegSensorValues)
#
# numpy.save("data/backLegSensorValues.npy", c.backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", c.frontLegSensorValues)
#
# numpy.save("data/targetAnglesBackLeg.npy", c.targetAnglesBackLeg)
# numpy.save("data/targetAnglesFrontLeg.npy", c.targetAnglesFrontLeg)

