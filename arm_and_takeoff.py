from dronekit import connect,VehicleMode

def arm_and_takeoff(aTargetAltitude):
	print "Basic pre-arm checks"
	while not vehicle.is_armable:
		print "Waiting for vehicle to initialise..."
		time.sleep(1)

	print "Arming Motors"
	vehicle.mode=VehicleMode("GUIDED")
	vehicle.armed=True

	while not vehicle.armed:
		print "Waiting for arming"
		time.sleep(1)

	while True:
		print "Altitude: ",vehicle.location.global_relative_frame.alt
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
			print "Reached target altitude"
			break
		time.sleep(1)

connection_string="/dev/ttyACM0"
baudrate=115200

vehicle=connect(connection_string,baud=baudrate,wait_ready=True)

arm_and_takeoff(20)
