import numpy as np
import optoMDC
from time import sleep
Mirror1 = optoMDC.connect("COM4")
Mirror2 = optoMDC.connect("COM5")

ch_0 = Mirror1.Mirror.Channel_0

ch_0.StaticInput.SetAsInput()                       
ch_0.InputConditioning.SetGain(1.0)                  
ch_0.SetControlMode(optoMDC.Units.XY)           
ch_0.LinearOutput.SetCurrentLimit(0.7)               

ch_0.Manager.CheckSignalFlow()                       

ch_1 = Mirror1.Mirror.Channel_1

ch_1.StaticInput.SetAsInput()                        
ch_1.InputConditioning.SetGain(1.0)                  
ch_1.SetControlMode(optoMDC.Units.XY)           
ch_1.LinearOutput.SetCurrentLimit(0.7)               

ch_1.Manager.CheckSignalFlow()                       

Mirror1_Y = Mirror1.Mirror.Channel_0.StaticInput

Mirror1_X = Mirror1.Mirror.Channel_1.StaticInput

######################################################################################################################################

ch_01 = Mirror2.Mirror.Channel_0

ch_01.StaticInput.SetAsInput()                        
ch_01.InputConditioning.SetGain(1.0)                  
ch_01.SetControlMode(optoMDC.Units.XY)           
ch_01.LinearOutput.SetCurrentLimit(0.7)               

ch_01.Manager.CheckSignalFlow()                       

ch_11 = Mirror2.Mirror.Channel_1

ch_11.StaticInput.SetAsInput()                        
ch_11.InputConditioning.SetGain(1.0)                  
ch_11.SetControlMode(optoMDC.Units.XY)           
ch_11.LinearOutput.SetCurrentLimit(0.7)               

ch_11.Manager.CheckSignalFlow()                       

Mirror2_Y = Mirror2.Mirror.Channel_0.StaticInput

Mirror2_X = Mirror2.Mirror.Channel_1.StaticInput


def laserMeasure():
    #Trigger laser to take measurement
    return 0

#For Mirror Distance finding, because the laser is only in 1 plane, we only need to control the X angle of the mirror

def findDistanceOA():
    #laser mirror setup to find OA
    return a

def findDistanceAB(a):
    #laser mirror setup to find AB
    return b

def findDistanceBC(a,b):
    #laser mirror setup to find BC
    return c

def findDistanceAC(a):
    #laser mirror setup to find AC
    return d

def triangulation(b,c,d):
    theta = np.arccos((d**2 + b**2 - c**2)/(2*b*d)) #in radians

    x = d * np.cos(theta)
    y = d * np.sin(theta)

    return x,y
