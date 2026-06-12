# Motion Safety Stack

## Overview

Motion Safety Stack is a ROS 2 Jazzy mini-project that demonstrates safe robot motion control using a modular node architecture.

The project combines:

- Robot-specific YAML profiles
- Environment-specific YAML profiles
- Velocity limiting
- Acceleration limiting
- Deceleration limiting
- Obstacle-based braking
- Watchdog-based emergency stopping
- Runtime monitoring
- Launch-based deployment

The goal is to simulate how a real robot motion pipeline enforces safety before commands reach the robot controller.

---

# Architecture

text robot.yaml environment.yaml         │         ▼     robot_info          │  velocity_source         │         ▼     /cmd_vel_raw          │         ▼   velocity_limiter          │         ▼    /cmd_vel_safe          │         ▼   velocity_watchdog          │         ▼       /cmd_vel          │         ▼   velocity_monitor 

---

# Nodes

## robot_info

Loads robot and environment configuration from YAML files.

Outputs:

- Robot information
- Effective speed limits
- Effective acceleration
- Effective stopping distance

---

## velocity_source

Generates simulated robot motion.

Behavior:

- Accelerate
- Drive straight
- Turn corners
- Simulate obstacle approach

Publishes:

text /cmd_vel_raw /obstacle_distance 

---

## velocity_limiter

Applies safety constraints.

Features:

- Linear speed limiting
- Angular speed limiting
- Acceleration limiting
- Deceleration limiting
- Obstacle-based emergency braking

Publishes:

text /cmd_vel_safe 

---

## velocity_watchdog

Monitors command availability.

Features:

- Timeout detection
- Emergency stop generation
- Command forwarding
- Configurable timeout

Publishes:

text / cmd_vel 

When commands stop arriving:

text linear.x = 0.0 angular.z = 0.0 

---

## velocity_monitor

Observes system behavior.

Displays:

- Raw command velocity
- Limited velocity
- Obstacle distance
- Braking status

---

# Configuration

## Robot Profile

Example:

yaml robot_info:   ros__parameters:      robot_name: go2      max_linear_speed: 3.5     max_angular_speed: 2.5      max_acceleration: 1.0     max_deceleration: 1.0      stopping_distance: 1.5      corner_linear_speed: 1.0     corner_angular_speed: 1.0 

---

## Environment Profile

Example:

yaml robot_info:   ros__parameters:      environment_name: indoor      linear_speed_factor: 0.5     angular_speed_factor: 0.6      acceleration_factor: 0.4     deceleration_factor: 1.0      stopping_distance_factor: 1.2 

---

# Launch

bash ros2 launch motion_safety_stack bringup.launch.py 

Specific robot:

bash ros2 launch motion_safety_stack bringup.launch.py robot:=go2 

Specific environment:

bash ros2 launch motion_safety_stack bringup.launch.py environment:=indoor 

---

# Validation

Verified Nodes:

bash ros2 node list 

Output:

text /robot_info /velocity_source /velocity_limiter /velocity_watchdog /velocity_monitor 

Verified Topics:

bash ros2 topic list 

Output:

text /cmd_vel_raw /cmd_vel_safe /cmd_vel /obstacle_distance 

---

# Safety Features

## Velocity Limiting

Restricts motion to configured robot limits.

## Acceleration Limiting

Prevents sudden speed changes.

## Deceleration Limiting

Controls braking behavior.

## Obstacle Braking

Stops the robot when obstacle distance falls below the configured threshold.

## Watchdog Protection

Stops the robot when command communication is lost.

---

# Learning Outcomes

This project demonstrates:

- ROS 2 node architecture
- Topic communication
- YAML parameter management
- Launch systems
- Runtime configuration
- Safety-critical motion control
- Monitoring and diagnostics
- Modular robotics software design

---

# Author

Shubham Verma

ROS 2 Learning Roadmap – Day 20 Mini Project