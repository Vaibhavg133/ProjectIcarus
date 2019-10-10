from dronekit import connect,VehicleMode
connectionString='/dev/ttyACM0'
baudrate=115200
vehicle=connect(connectionString,baud=baudrate,wait_ready=True)
print "Ardupilot Firmware Version: %s" % vehicle.version
print "Ardupilot Capabilities(FTP): %s" % vehicle.capabilities.ftp
print "Global Location: %s" % vehicle.location.global_frame
print "Global Location (relative altitude): %s" % vehicle.location.local_frame
print "Altitude: %s" % vehicle.altitude
print "Velocity: %s" % vehicle.velocity
print "GPS: %s" % vehicle.gps_0
print "GroundSpeed: %s" %vehicle.groundspeed
print "Airspeed: %s" % vehicle.airspeed
print "Gimbal Status: %s" % vehicle.gimbal
print "Battery: %s" % vehicle.battery
print "EKF OK ? %s" % vehicle.ekf_ok
print "Last Heartbeat: %s" % vehicle.last_heartbeat
print "Rangefinder Distance: %s" % vehicle.rangefinder.distance
print "Rangefinder Voltage: %s" % vehicle.rangefinder.voltage
print "Heading: %s" % vehicle.heading
print "Is Armable: %s" % vehicle.is_armable
print "System Status: %s" % vehicle.system_status.state
print "Mode: %s" % vehicle.mode.name
print "Armed: %s" % vehicle.armed
vehicle.close()
