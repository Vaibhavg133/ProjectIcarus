from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
import math
import argparse

def connectMyCopter():
	parser = argparse.ArgumentParser(description="commands")
	parser.add_argument('--connect')
	args = parser.parse_args()
	connection_string = args.connect
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle
# python connection_template.py --connect 127.0.0.1:14550

vehicle=connectMyCopter()
