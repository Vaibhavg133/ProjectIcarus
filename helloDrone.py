from dronekit import connect,VehicleMode

connectionString="/dev/ttyACM0"   #Use ttyACM0 for USB connection and ttyAMA0 for serial connection (Telemetry Connection) 
#use sitl.connection_string() for SITL and for this you need to import dronekit_sitl
baudrate=115200 #for USB use 115200 and for serial 57600
print("Connecting to the vehicle on:%s"%(connectionString),)

vehicle=connect(connectionString,baud=baudrate,wait_ready=True)

print("Get some vehicle attribute values:")
print("GPS: %s" % vehicle.gps_0)
print("Battery: %s" % vehicle.battery)
print("Last Heartbeat: %s" % vehicle.last_heartbeat)
print("Is Armable? : %s" % vehicle.is_armable)
print("System Status: %s" % vehicle.system_status.state)
print("Mode: %s" % vehicle.mode.name)

vehicle.close()

print("Completed")
