import numpy
import matplotlib.pyplot

#load in target angles vector
targetAngleValuesBackLeg = numpy.load("data/targetAnglesBackLeg.npy")
targetAngleValuesFrontLeg = numpy.load("data/targetAnglesFrontLeg.npy")
#print(targetAngleValues)


#plot target angle vector
matplotlib.pyplot.plot(targetAngleValuesBackLeg)
matplotlib.pyplot.plot(targetAngleValuesFrontLeg)


#display legend
matplotlib.pyplot.legend()

#display the graph
matplotlib.pyplot.show()






###load in back leg sensor
##backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
##print(backLegSensorValues)
###load in front leg sensor
##frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
##print(frontLegSensorValues)
##
###plot front and back leg sensor points
##matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 2)
##matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg", linewidth = 2)
##
###display legend
##matplotlib.pyplot.legend()
##
###display the graph
##matplotlib.pyplot.show()
