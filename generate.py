import pyrosim.pyrosim as pyrosim

#x1 = 0
#y1 = 0
#z1 = 0.5
#x2 = 0
#y2 = 1
#z2 = 1.5

#code for 6x6 of stack of blocks decreasing in size
#for a in range(0, 6):
 #   for b in range(0, 6):
  #      for i in range(11, 1, -1):
   #         pyrosim.Send_Cube(name="Box", pos=[a, b,((-i+11.5)*.9)],
    #                  size=[(i*0.9)/10, (i*0.9)/10, (i*0.9)/10])    


#create world
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #create cube away from center
    pyrosim.Send_Cube(name="Box", pos=[4, 0, .5] , size=[1, 1, 1])
    pyrosim.End()   

#create robot
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    #create back leg
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[1, 1, 1])
    
    #create joint between back leg and torso
    pyrosim.Send_Joint( name = "Torso_BackLeg" ,
                        parent= "Torso" , child = "BackLeg" ,
                        type = "revolute", position = "0.5 0 1")
    
    #create torso    
    pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5] , size=[1, 1, 1])
    
    #create joint between front leg and torso
    pyrosim.Send_Joint( name = "Torso_FrontLeg" ,
                        parent= "Torso" , child = "FrontLeg" ,
                        type = "revolute", position = "1.5 0 1")
    
        #create front leg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[1, 1, 1])
    
    pyrosim.End()





#function calls
Create_World()
Create_Robot()
