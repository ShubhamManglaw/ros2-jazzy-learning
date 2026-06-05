# Day 09 — Custom Message Build

Date: June 2026  
Phase: ROS Communication Layer  
Topic: Custom Message Creation and Usage

---

# Objective

Learn how to create custom ROS 2 messages, configure interface packages, generate message code, and use custom messages inside Python nodes.

---

# Concepts Covered

- ROS Interface Packages
- Custom Messages (.msg)
- Message Generation Pipeline
- package.xml Configuration
- CMakeLists.txt Configuration
- rosidl Interface Generation
- Interface Dependencies
- Generated Message Classes
- Custom Message Publishing

---

# Big Picture

Until now I was using built-in ROS messages:

text std_msgs/String std_msgs/Int32 geometry_msgs/Twist sensor_msgs/LaserScan 

Today I learned how to create my own message type.

ROS workflow:

text RobotStatus.msg         ↓ colcon build         ↓ Generated Python/C++ Message Classes         ↓ Import Into Nodes         ↓ Publish / Subscribe 

---

# Created Interface Package

Created a dedicated interface package:

bash ros2 pkg create my_robot_interfaces --build-type ament_cmake 

Workspace structure:

text src/ ├── my_first_pkg └── my_robot_interfaces 

Reason:

- Keep interfaces separate from nodes
- Reusable across multiple packages
- Professional ROS package structure

---

# Created Custom Message

File:

text my_robot_interfaces/msg/RobotStatus.msg 

Contents:

text std_msgs/Header header  float32 battery_percentage  uint8 MODE_OFFLINE=0 uint8 MODE_MANUAL=1 uint8 MODE_AUTONOMOUS=2 uint8 MODE_CHARGING=3  uint8 robot_mode  bool emergency_stop  float32 linear_velocity_mps float32 angular_velocity_radps 

---

# Understanding the Message

## Header

text std_msgs/Header header 

Provides:

text stamp frame_id 

Used for timestamps and coordinate frame information.

---

## Battery Percentage

text float32 battery_percentage 

Represents current battery level.

---

## Robot Modes

text MODE_OFFLINE MODE_MANUAL MODE_AUTONOMOUS MODE_CHARGING 

Allows readable robot states instead of magic numbers.

Example:

python msg.robot_mode = RobotStatus.MODE_AUTONOMOUS 

instead of:

python msg.robot_mode = 2 

---

## Safety State

text bool emergency_stop 

Represents E-Stop status.

---

## Motion Information

text float32 linear_velocity_mps float32 angular_velocity_radps 

Units included in field names to remove ambiguity.

---

# package.xml Changes

Added:

xml <buildtool_depend>rosidl_default_generators</buildtool_depend>  <depend>std_msgs</depend>  <exec_depend>rosidl_default_runtime</exec_depend>  <member_of_group>rosidl_interface_packages</member_of_group> 

Purpose:

- Enable message generation
- Access Header definition
- Export generated interfaces
- Register package as interface package

---

# CMakeLists.txt Changes

Added:

cmake find_package(rosidl_default_generators REQUIRED) find_package(std_msgs REQUIRED) 

Message generation:

cmake rosidl_generate_interfaces(${PROJECT_NAME}   "msg/RobotStatus.msg"   DEPENDENCIES std_msgs ) 

Export:

cmake ament_export_dependencies(rosidl_default_runtime) 

Purpose:

Tell ROS to generate code from RobotStatus.msg.

---

# Build Process

Build command:

bash cd ~/ros2-jazzy-learning  colcon build --packages-select my_robot_interfaces 

Result:

text Starting >>> my_robot_interfaces Finished <<< my_robot_interfaces 

Successful build means:

- Message syntax valid
- Dependencies resolved
- Interface generated correctly

---

# Interface Verification

Command:

bash source install/setup.bash  ros2 interface show my_robot_interfaces/msg/RobotStatus 

Output confirmed ROS recognized the custom message.

---

# Using the Message in Python

Import:

python from my_robot_interfaces.msg import RobotStatus 

Important realization:

text RobotStatus.msg         ↓ colcon build         ↓ Generated RobotStatus Class         ↓ Python Import 

The import does not load the .msg file directly.

It loads the generated Python class.

---

# Custom Publisher Node

Created:

text robot_status_publisher.py 

Publisher:

python self.publisher_ = self.create_publisher(     RobotStatus,     'robot_status',     10 ) 

Timer:

python self.timer = self.create_timer(     1.0,     self.publish_status ) 

Message creation:

python msg = RobotStatus() 

Field assignment:

python msg.battery_percentage = 85.0 msg.robot_mode = RobotStatus.MODE_AUTONOMOUS msg.emergency_stop = False msg.linear_velocity_mps = 0.5 msg.angular_velocity_radps = 0.1 

Publish:

python self.publisher_.publish(msg) 

---

# Package Dependency Integration

Added dependency:

xml <depend>my_robot_interfaces</depend> 

inside:

text my_first_pkg/package.xml 

Reason:

Allow importing:

python from my_robot_interfaces.msg import RobotStatus 

inside node packages.

---

# Setup.py Changes

Registered executable:

python 'robot_status_publisher = my_first_pkg.robot_status_publisher:main' 

Allows execution using:

bash ros2 run my_first_pkg robot_status_publisher 

---

# Runtime Verification

Verified topic exists:

bash ros2 topic list 

Output:

text /robot_status 

Echoed topic:

bash ros2 topic echo /robot_status 

Output:

yaml battery_percentage: 85.0 robot_mode: 2 emergency_stop: false linear_velocity_mps: 0.5 angular_velocity_radps: 0.1 

Custom message successfully transmitted through ROS.

---

# Key Learnings

1. Custom messages are defined in .msg files.
2. ROS generates message code during build.
3. Interface packages should be separate from node packages.
4. package.xml and CMakeLists.txt control message generation.
5. Generated messages behave exactly like built-in ROS messages.
6. Constants improve readability and maintainability.
7. Custom interfaces can be imported into any ROS package.

---

# Common Mistakes Encountered

- Confusion between .msg file and generated class.
- Incorrect setup.py package path.
- Logger method typo.
- Understanding package dependencies.
- Understanding message generation workflow.

---

# Final Understanding

Most important realization:

text .msg file       ↓ Build System       ↓ Generated Message Class       ↓ Import       ↓ Publish       ↓ ROS Topic 

This is the foundation for future custom messages, services, and actions.

---

# Completion Status

Completed:

- Created interface package
- Created RobotStatus.msg
- Configured package.xml
- Configured CMakeLists.txt
- Generated interface
- Verified interface
- Imported custom message
- Published custom message
- Verified topic transmission

Status: COMPLETE ✅