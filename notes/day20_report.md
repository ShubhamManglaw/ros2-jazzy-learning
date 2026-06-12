# Day 20 Report — Motion Safety Stack Mini Project

## Objective

Build a complete ROS 2 motion safety subsystem integrating launch files, YAML configuration, runtime parameters, monitoring, diagnostics, and safety mechanisms.

---

## System Architecture

velocity_source

↓

/cmd_vel_raw

↓

velocity_limiter

↓

/cmd_vel_safe

↓

velocity_watchdog

↓

/cmd_vel

↓

velocity_monitor

---

## Components Built

### robot_info

Loads robot and environment profiles from YAML files.

Responsibilities:

- Read robot specifications
- Read environment configuration
- Compute effective operating limits
- Display final runtime configuration

### velocity_source

Simulates robot commands.

Responsibilities:

- Publish velocity commands
- Generate test inputs
- Provide repeatable motion behavior

### velocity_limiter

Safety layer for motion commands.

Responsibilities:

- Enforce linear speed limits
- Enforce angular speed limits
- Validate runtime parameter changes
- Publish safe velocity commands

### velocity_watchdog

Communication safety node.

Responsibilities:

- Monitor command stream
- Detect command loss
- Trigger emergency stop
- Prevent runaway robot motion

### velocity_monitor

System diagnostics node.

Responsibilities:

- Observe final robot commands
- Verify system output
- Provide operator feedback

---

## YAML Configuration

Robot-specific parameters:

- robot_name
- robot_type
- robot_weight_kg
- payload_capacity_kg
- max_linear_speed
- max_angular_speed
- max_acceleration
- stopping_distance

Environment-specific parameters:

- environment_name
- linear_speed_factor
- angular_speed_factor
- acceleration_factor
- stopping_distance_factor

---

## Key Features

### Dynamic Configuration

No robot values are hardcoded.

All configuration is loaded from YAML files.

### Runtime Parameter Tuning

Verified:

bash ros2 param set ros2 param get ros2 param describe ros2 param list 

### Parameter Validation

Velocity limiter rejects invalid values.

Examples:

- max_linear_speed < 0
- max_linear_speed > 5.0
- max_angular_speed > 10.0

### Emergency Stop

Watchdog automatically publishes:

text linear.x = 0.0 angular.z = 0.0 

after timeout.

---

## Failure Testing

### Test 1 — Stop Command Publisher

Result:

Watchdog timeout triggered.

Robot safely stopped.

### Test 2 — Invalid Parameter

Result:

Parameter rejected.

System continued running safely.

### Test 3 — Runtime Parameter Change

Result:

Velocity limiter updated behavior immediately.

### Test 4 — YAML Profile Change

Result:

Different robot/environment profiles loaded correctly.

---

## Diagnostics Used

bash ros2 node list ros2 topic list ros2 topic echo ros2 topic hz ros2 param list ros2 doctor rqt_graph 

---

## Engineering Reflection

### Why are watchdog systems important?

They prevent robots from continuing motion after communication failure.

### What failures occur without watchdogs?

- Runaway robots
- Network failure hazards
- Unsafe autonomous behavior

### Most safety-critical component?

velocity_watchdog

It provides the final emergency stop mechanism.

### Real-world improvements

- Diagnostics messages
- Lifecycle nodes
- Safety states
- Hardware E-stop integration
- Sensor fusion

---

## Outcome

Successfully engineered a complete ROS 2 Motion Safety Stack using:

- Launch files
- YAML configuration
- Parameters
- Runtime tuning
- Safety monitoring
- Diagnostics
- Emergency stopping

This project represents the first portfolio-quality ROS 2 subsystem built during the roadmap.