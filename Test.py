#to output a sinusoid on Channel_0 in open-loop (current) mode...

from optoMDC.registers.mre2_registers import ResonantAmplitudeControl 

import optoMDC
mre2 = optoMDC.connect()

#To configure channel in open loop mode...

ch_0 = mre2.Mirror.Channel_0

ch_0.SignalGenerator.SetAsInput()                    # (1) here we tell the Manager that the sig gen is the desired input
ch_0.InputConditioning.SetGain(1.0)                  # (2) here we tell the Manager some input conditioning parameters
ch_0.SetControlMode(optoMDC.Units.CURRENT)           # (3) here we tell the Manager that our input will be in units of current. This is open-loop mode
ch_0.LinearOutput.SetCurrentLimit(0.7)               # (4) here we tell the Manager to limit the current to 700mA (default)

ch_0.Manager.CheckSignalFlow()                       # This is a useful method to make sure the signal flow is configured correctly.

ch_1 = mre2.Mirror.Channel_1

ch_1.SignalGenerator.SetAsInput()                    # (1) here we tell the Manager that the sig gen is the desired input
ch_1.InputConditioning.SetGain(1.0)                  # (2) here we tell the Manager some input conditioning parameters
ch_1.SetControlMode(optoMDC.Units.CURRENT)           # (3) here we tell the Manager that our input will be in units of current. This is open-loop mode
ch_1.LinearOutput.SetCurrentLimit(0.7)               # (4) here we tell the Manager to limit the current to 700mA (default)

ch_1.Manager.CheckSignalFlow()                       # This is a useful method to make sure the signal flow is configured correctly.


#The channel is configured. The output of the Signal Generator will now proceed through the signal flow mentioned above.

#Therefore, next we will configure the output of the Signal Generator.

sg_0 = mre2.Mirror.Channel_0.SignalGenerator

sg_0.SetUnit(optoMDC.Units.CURRENT)                 # here we set the sig gen to output in units of current (This must match the control mode!)
sg_0.SetShape(optoMDC.Waveforms.SINUSOIDAL)         # here we set the sig gen output waveform type
sg_0.SetFrequency(10.0)                             # here we set the frequency in Hz
sg_0.SetAmplitude(0.100)                            # here we set the amplitude in Amps
sg_0.Run()

sg_1 = mre2.Mirror.Channel_1.SignalGenerator

sg_1.SetUnit(optoMDC.Units.CURRENT)                 # here we set the sig gen to output in units of current (This must match the control mode!)
sg_1.SetShape(optoMDC.Waveforms.SINUSOIDAL)         # here we set the sig gen output waveform type
sg_1.SetFrequency(10.0)                             # here we set the frequency in Hz
sg_1.SetAmplitude(0.100)                            # here we set the amplitude in Amps
sg_1.Run()
