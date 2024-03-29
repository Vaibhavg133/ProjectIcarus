"""
Test of connection with an actual ardupilot
"""

from dronekit import connect, VehicleMode
import time
import dronekit_sitl
connection_string="/dev/ttyACM0"
baud_rate = 115200
print(">>>> Connecting with the UAV <<<")
vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)

print('Position: %s'% vehicle.location.global_relative_frame)

#- Read the actual attitude roll, pitch, yaw
print('Attitude: %s'% vehicle.attitude)

#- Read the actual velocity (m/s)
print('Velocity: %s'%vehicle.velocity) #- North, east, down

#- When did we receive the last heartbeat
print('Last Heartbeat: %s'%vehicle.last_heartbeat)

#- Is the vehicle good to Arm?
print('Is the vehicle armable: %s'%vehicle.is_armable)

#- Which is the total ground speed?   Note: this is settable
print('Groundspeed: %s'% vehicle.groundspeed) #(%)

#- What is the actual flight mode?    Note: this is settable
print('Mode: %s'% vehicle.mode.name)

#- Is the vehicle armed               Note: this is settable
print('Armed: %s'%vehicle.armed)

#- Is thestate estimation filter ok?
print('EKF Ok: %s'%vehicle.ekf_ok)



#----- Adding a listener
#-- dronekit updates the variables as soon as it receives an update from the UAV
#-- you can define a callback function for predefined messages or define one for
#-- any mavlink message 

def attitude_callback(self, attr_name, value):
    print(vehicle.attitude)


print("")
print("Adding an attitude listener")
vehicle.add_attribute_listener('attitude', attitude_callback) #-- message type, callback function
time.sleep(5)

#--- Now we print the attitude from the callback for 5 seconds, then we remove the callback
vehicle.remove_attribute_listener('attitude', attitude_callback) #(.remove)


#--- You can create a callback even with decorators, check the documentation out for more details



#---- PARAMETERS
print("Maximum Throttle: %d"%vehicle.parameters['THR_MIN']) 

#-- You can read and write the parameters
vehicle.parameters['THR_MIN'] = 50
time.sleep(1)
print("Maximum Throttle: %d"%vehicle.parameters['THR_MIN'])



#--- Now we close the simulation
vehicle.close()
print("done")
