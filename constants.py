import numpy
import math

amplitudeBackLeg = numpy.pi/5
frequencyBackLeg  = 20
phaseOffsetBackLeg = 0

amplitudeFrontLeg = -numpy.pi/4
frequencyFrontLeg  = 20
phaseOffsetFrontLeg = 0

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

min = -(math.pi)/4
max = +(math.pi)/4

targetAnglesBackLeg = numpy.linspace(-numpy.pi, numpy.pi, 1000)

targetAnglesFrontLeg = numpy.linspace(-numpy.pi, numpy.pi, 1000)
