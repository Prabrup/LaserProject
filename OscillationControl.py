#to output a sinusoid on Channel_0 in open-loop (current) mode...

from optoMDC.registers.mre2_registers import ResonantAmplitudeControl 

import optoMDC
mre2 = optoMDC.connect()

#Initialise first mirror and boths its axis in open loop

ch_0 = mre2.Mirror.Channel_0

ch_0.SignalGenerator.SetAsInput()                    
ch_0.InputConditioning.SetGain(1.0)
ch_0.SetControlMode(optoMDC.Units.CURRENT)    
ch_0.LinearOutput.SetCurrentLimit(0.7)               

ch_0.Manager.CheckSignalFlow()                      

ch_1 = mre2.Mirror.Channel_1

ch_1.SignalGenerator.SetAsInput()              
ch_1.InputConditioning.SetGain(1.0)       
ch_1.SetControlMode(optoMDC.Units.CURRENT)     
ch_1.LinearOutput.SetCurrentLimit(0.7)           

ch_1.Manager.CheckSignalFlow()               


#Initialise second mirror and boths its axis in open loop
sg_0 = mre2.Mirror.Channel_0.SignalGenerator

sg_0.SetUnit(optoMDC.Units.CURRENT)                
sg_0.SetShape(optoMDC.Waveforms.TRIANGLE)        
sg_0.SetFrequency(2)                           
sg_0.SetAmplitude(0.010)                            
sg_0.Run()

sg_1 = mre2.Mirror.Channel_1.SignalGenerator

sg_1.SetUnit(optoMDC.Units.CURRENT)                
sg_1.SetShape(optoMDC.Waveforms.PULSE)        
sg_1.SetFrequency(2.0)                            
sg_1.SetAmplitude(0.010)                            
sg_1.Run()
