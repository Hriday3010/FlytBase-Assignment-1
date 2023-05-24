import time
from flyt_python import api
drone = api.navigation()

#10s for sensor initialisation and callibration
time.sleep(3)

#Arm the Drone
drone.arm()

print 'Taking Off'
drone.take_off(5.0)

print 'Mission Underway'
drone.position_set(6.5,0,95.082, relative=False)
drone.position_set(0,6.5,95.081, relative=False)
drone.position_set(-6.5,0,95.082, relative=False)
drone.position_set(0,-6.5,95.084, relative=False)

print 'Landing'
drone.land(async=False)

#Disarm the Drone
drone.disarm()

#Disconnect from instance
drone.disconnect()
