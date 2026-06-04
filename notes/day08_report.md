# Day 08 — Message Design

Date: June 2026  
Phase: Advanced Engineering  
Topic: Message Design

---

# Objective

Understand how ROS 2 messages are designed and why message types act as contracts between publishers and subscribers.

The goal was to learn how to select appropriate standard message types, understand their structure, and design meaningful custom messages for robotics applications.

---

# Concepts Covered

- ROS Messages
- Message Types
- Data Contracts
- Standard ROS Interfaces
- Message Structure
- Field Types
- Units and Naming
- Custom Message Design
- Interface Inspection

---

# Big Picture

A ROS topic is not only a topic name.

Every topic also has a message type that defines the structure of the data being exchanged.

Examples:

text /chatter   → std_msgs/msg/String  /cmd_vel   → geometry_msgs/msg/Twist  /scan      → sensor_msgs/msg/LaserScan  /odom      → nav_msgs/msg/Odometry 

Publishers and subscribers must agree on both:

- Topic Name
- Message Type

Otherwise communication cannot occur.

---

# Interface Inspection Commands

Used the following commands:

bash ros2 interface show std_msgs/msg/String  ros2 interface show std_msgs/msg/Int32  ros2 interface show geometry_msgs/msg/Twist  ros2 interface show sensor_msgs/msg/LaserScan 

---

# Message Analysis

## String Message

Command:

bash ros2 interface show std_msgs/msg/String 

Output:

text string data 

Observation:

The message contains only a single field named data.

Useful for learning but lacks semantic meaning for larger robotics systems.

---

## Int32 Message

Command:

bash ros2 interface show std_msgs/msg/Int32 

Output:

text int32 data 

Observation:

The message contains only a single integer field.

This is sufficient for simple examples but does not explain what the value represents.

Example:

text data = 42 

The meaning is unclear.

Possible meanings:

- Battery percentage
- Encoder ticks
- RPM
- Object count

A better design gives fields meaningful names.

---

## Twist Message

Command:

bash ros2 interface show geometry_msgs/msg/Twist 

Output:

text Vector3 linear Vector3 angular 

Expanded structure:

text linear.x linear.y linear.z  angular.x angular.y angular.z 

Typical differential drive usage:

text linear.x  → Forward velocity (m/s)  angular.z → Rotational velocity (rad/s) 

Why Twist is better than String:

- Structured data
- Typed fields
- Standard ROS interface
- Easier debugging
- No string parsing required
- Supported by ROS navigation tools

---

## LaserScan Message

Command:

bash ros2 interface show sensor_msgs/msg/LaserScan 

Important fields:

text header  angle_min angle_max angle_increment  range_min range_max  ranges[] intensities[] 

### Header

Contains:

text stamp frame_id 

Meaning:

text stamp    → When the scan was taken  frame_id → Where the scan was taken 

### Angle Information

text angle_min angle_max angle_increment 

Defines the geometry of the scan.

### Range Information

text range_min range_max 

Defines valid measurement limits.

### Range Array

text float32[] ranges 

Stores measured obstacle distances.

This is how many robots perceive surrounding objects.

---

# Message Design Principles

Good messages should be:

- Clear
- Typed
- Minimal
- Stable
- Reusable
- Easy to inspect
- Easy to debug

Avoid:

- Encoding structured data as strings
- Ambiguous field names
- Missing units
- Excessively large messages
- Constantly changing message definitions

---

# Importance of Units

Units should be obvious from field names.

Weak:

text float32 speed 

Better:

text float32 speed_mps 

Weak:

text float32 angular_velocity 

Better:

text float32 angular_velocity_radps 

Robotics bugs are frequently caused by unit confusion.

---

# Custom Message Design Exercise

Designed a custom RobotStatus message.

text std_msgs/Header header  float32 battery_percentage  uint8 MODE_OFFLINE = 0 uint8 MODE_MANUAL = 1 uint8 MODE_AUTONOMOUS = 2 uint8 MODE_CHARGING = 3  uint8 robot_mode  bool emergency_stop  float32 linear_velocity_mps float32 angular_velocity_radps 

Design choices:

- Header for timestamps
- Battery monitoring
- Enumerated robot modes
- Emergency stop status
- Explicit velocity units

---

# Key Learnings

1. Every ROS topic has a message type.
2. Message types act as contracts between nodes.
3. Standard ROS messages should be preferred whenever possible.
4. Twist is a better representation of robot velocity than strings.
5. Message fields should have clear meaning and units.
6. Custom messages should only be created when standard messages are insufficient.
7. Good message design improves debugging and maintainability.

---

# Commands Used

bash ros2 interface list  ros2 interface show std_msgs/msg/String  ros2 interface show std_msgs/msg/Int32  ros2 interface show geometry_msgs/msg/Twist  ros2 interface show sensor_msgs/msg/LaserScan 

---

# Reflection

Today was less about writing ROS code and more about understanding how robotics software communicates information.

The most important lesson was realizing that messages are contracts between nodes. Good message design improves clarity, debugging, reuse, and long-term maintainability.

I also learned to think about field names, units, and data meaning rather than focusing only on data types.

---

# Completion Criteria

Completed:

- Inspected String message
- Inspected Int32 message
- Inspected Twist message
- Inspected LaserScan message
- Compared good vs bad message design
- Studied message naming conventions
- Studied unit conventions
- Designed a custom RobotStatus message

Status: COMPLETE