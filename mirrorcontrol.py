import optoMDC

import keyboard

import time

import math

 

mre2 = optoMDC.connect("COM3")

 

ch_0 = mre2.Mirror.Channel_0

ch_0.StaticInput.SetAsInput()                        # (1) here we tell the Manager that we will use a static iq1nput

ch_0.InputConditioning.SetGain(1.0)                  # (2) here we tell the Manager some input conditioning parameters

ch_0.SetControlMode(optoMDC.Units.XY)                # (3) here we tell the Manager that our input will be in units of current

ch_0.LinearOutput.SetCurrentLimit(0.7)               # (4) here we tell the Manager to limit the current to 700mA (default)

ch_0.Manager.CheckSignalFlow()                       # This is a useful method to make sure the signal flow is configured correctly.

 

ch_1 = mre2.Mirror.Channel_1

ch_1.StaticInput.SetAsInput()                        # (1) here we tell the Manager that we will use a static input

ch_1.InputConditioning.SetGain(1.0)                  # (2) here we tell the Manager some input conditioning parameters

ch_1.SetControlMode(optoMDC.Units.XY)                # (3) here we tell the Manager that our input will be in units of current

ch_1.LinearOutput.SetCurrentLimit(0.7)               # (4) here we tell the Manager to limit the current to 700mA (default)

ch_1.Manager.CheckSignalFlow()                       # This is a useful method to make sure the signal flow is configured correctly.

 

# Configuration for two mirrors

ch_0 = mre2.Mirror.Channel_0.StaticInput

ch_1 = mre2.Mirror.Channel_1.StaticInput

 

# Set initial angles for the mirrors

ch_0.SetXY(0.0)  # Initial x angle for mirror 1

ch_1.SetXY(0.0)  # Initial y angle for mirror 1

 

# New names for the StaticInput

ch_0_input = mre2.Mirror.Channel_0.StaticInput

ch_1_input = mre2.Mirror.Channel_1.StaticInput

 

# Global variables to store current channels

current_channel_x = None

current_channel_y = None

 

def select_mirror():

    global current_channel_x, current_channel_y

    while True:

        if keyboard.is_pressed('1'):

            current_channel_x = ch_0_input

            current_channel_y = ch_1_input

            print("Selected Mirror 1")

            break

        time.sleep(0.1)

 

#def copy_position():

 #   global saved_x, saved_y

 

#def paste_position():

 #   saved_x = angle_x

 #   saved_y = angle_y

 

def control_mirror():

    angle_x = 0.0

    angle_y = 0.0

    step_size = 0.05

    adjustment_value = 0.002

 

    select_mirror()  # Call the function to select the mirror first

 

    while True:

        if keyboard.is_pressed('q'):  # Check if 'q' is pressed to toggle mirror selection

            print("Select a mirror")        

            select_mirror()

      #  if keyboard.is_pressed('c'):  # Check if 'q' is pressed to toggle mirror selection

      #      copy_position()

      #      print("Position saved")  

      #  if keyboard.is_pressed('p'):  # Check if 'q' is pressed to toggle mirror selection

      #      paste_position()

      #      print("Position called from memory")      

        if keyboard.is_pressed('left'):

            angle_x -= step_size

            current_channel_x.SetXY(angle_x)

            print(f"Angle x = {(angle_x*(180/math.pi))} deg")

        elif keyboard.is_pressed('right'):

            angle_x += step_size

            current_channel_x.SetXY(angle_x)

            print(f"Angle x = {(angle_x*(180/math.pi))} deg")

        elif keyboard.is_pressed('down'):

            angle_y -= step_size

            current_channel_y.SetXY(angle_y)

            print(f"Angle y = {(angle_y*(180/math.pi))} deg")

        elif keyboard.is_pressed('up'):

            angle_y += step_size

            current_channel_y.SetXY(angle_y)

            print(f"Angle y = {(angle_y*(180/math.pi))} deg")

        elif keyboard.is_pressed('w'):

            step_size += adjustment_value

            print(f"Step size increased to {step_size}")

        elif keyboard.is_pressed('s'):

            step_size -= adjustment_value

            print(f"Step size decreased to {step_size}")

        elif keyboard.is_pressed('x'):

            break

 

        time.sleep(0.1)

 

control_mirror()  # Call the function to start controlling the mirror

