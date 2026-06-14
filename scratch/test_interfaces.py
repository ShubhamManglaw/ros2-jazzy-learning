from my_robot_interfaces.msg import RobotStatus
from my_robot_interfaces.srv import SetMode

status = RobotStatus()
request = SetMode.Request()

print("Message import successful")
print("Service import successful")
