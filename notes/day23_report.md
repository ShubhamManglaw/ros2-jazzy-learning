Day 23 Report — Interface Package Engineering

Objective

Build a reusable ROS 2 communication layer by creating a dedicated interface package containing custom messages, services, and actions.

⸻

Package Created

my_robot_interfaces

⸻

Interfaces Implemented

Messages

RobotStatus.msg

std_msgs/Header header
float32 battery_voltage
uint8 MODE_OFFLINE=0
uint8 MODE_MANUAL=1
uint8 MODE_AUTONOMOUS=2
uint8 MODE_CHARGING=3
uint8 robot_mode
bool emergency_stop

RobotTelemetry.msg

std_msgs/Header header
string robot_name
float32 battery_percentage
float32 cpu_usage_percentage
float32 sensor1_temp
float32 sensor2_temp
float32 sensor3_temp
float32 sensor4_temp

Services

SetMode.srv

uint8 desired_mode
---
bool success
uint8 current_mode

ResetRobot.srv

bool confirm
---
bool success

Actions

NavigateToPose.action

float64 x
float64 y
float64 yaw
---
bool success
string message
---
float64 distance_remaining

⸻

Build Configuration

Updated package.xml with:

* rosidl_default_generators
* rosidl_default_runtime
* std_msgs
* action_msgs
* rosidl_interface_packages group membership

Updated CMakeLists.txt to generate all custom interfaces using rosidl_generate_interfaces().

⸻

Verification

Successfully built package:

colcon build --packages-select my_robot_interfaces

Verified generated interfaces:

ros2 interface show my_robot_interfaces/msg/RobotStatus
ros2 interface show my_robot_interfaces/msg/RobotTelemetry
ros2 interface show my_robot_interfaces/srv/SetMode
ros2 interface show my_robot_interfaces/srv/ResetRobot
ros2 interface show my_robot_interfaces/action/NavigateToPose

Created Python verification script and confirmed generated classes can be imported successfully.

Output:

All imports successful

⸻

Key Learnings

* Interface packages should remain independent from node implementations.
* Messages are used for continuous data streams.
* Services are used for request-response interactions.
* Actions are used for long-running tasks with feedback.
* ROSIDL automatically generates language-specific code from interface definitions.
* Custom interfaces serve as reusable communication contracts across packages.

⸻

Engineering Outcome

Designed and implemented a reusable ROS 2 communication layer consisting of custom messages, services, and actions. Successfully generated and verified all interfaces, establishing a scalable architecture for future Action Server, Action Client, and robot management systems.

Status

Completed Successfully

Progress: 100%