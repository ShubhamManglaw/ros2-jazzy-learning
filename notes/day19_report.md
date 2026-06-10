# Day 19 Report – Diagnostics & Inspection

## Objective

Learn how to inspect, debug, validate, and troubleshoot a ROS 2 system using engineering workflows rather than trial-and-error debugging.

---

## System Used

Package: robot_bringup

Launch File:

bash ros2 launch robot_bringup bringup.launch.py 

Nodes:

- velocity_source
- velocity_limiter
- velocity_monitor

---

## Graph Inspection

### Node List

text /velocity_source /velocity_limiter /velocity_monitor 

### Node Relationships

velocity_source:
- Publishes: /cmd_vel_raw

velocity_limiter:
- Subscribes: /cmd_vel_raw
- Publishes: /cmd_vel

velocity_monitor:
- Subscribes: /cmd_vel

System data flow:

velocity_source → /cmd_vel_raw → velocity_limiter → /cmd_vel → velocity_monitor

---

## Topic Inspection

### Topic List

text /cmd_vel /cmd_vel_raw /parameter_events /rosout 

### Topic Information

/cmd_vel_raw

text Publisher count: 1 Subscription count: 1 

/cmd_vel

text Publisher count: 1 Subscription count: 1 

Observation:
- Topic connectivity was healthy.
- All expected publishers and subscribers were present.

---

## Topic Frequency Diagnostics

Command:

bash ros2 topic hz /cmd_vel_raw 

Observed Rate:

text ~1.0 Hz 

Observations:
- Stable message delivery.
- No dropped messages observed.
- Publisher timing remained consistent.

---

## System Health Check

Command:

bash ros2 doctor 

Result:

text All 5 checks passed 

Observations:
- ROS installation healthy.
- DDS communication functioning correctly.
- Environment configured properly.
- Multiple package update notifications were reported but no critical issues were detected.

---

## Parameter Inspection

### Parameter List

text /velocity_limiter:   max_angular_speed   max_linear_speed 

### Parameter Values

text max_linear_speed = 0.3 max_angular_speed = 0.5 

### Parameter Dump

yaml /velocity_limiter:   ros__parameters:     max_angular_speed: 0.5     max_linear_speed: 0.3 

Observations:
- YAML configuration loaded correctly.
- Runtime parameters matched expected values.
- Parameter verification confirmed proper launch configuration.

---

## Failure Injection

### Scenario

The velocity_source node was intentionally terminated.

Command:

bash pkill -f velocity_source 

### Results

Node List:

text /velocity_limiter /velocity_monitor 

Topic Information:

text /cmd_vel_raw Publisher count: 0 Subscription count: 1 

Topic Frequency:

text No messages received 

Diagnosis:
- velocity_source was no longer publishing.
- velocity_limiter remained subscribed to /cmd_vel_raw.
- Message flow stopped completely.
- Root cause identified successfully through graph inspection and topic diagnostics.

Recovery:
- Relaunch the system using the bringup launch file.

---

## Key Learnings

- ros2 node list provides the fastest overview of system health.
- ros2 node info reveals publisher and subscriber relationships.
- ros2 topic info verifies communication paths.
- ros2 topic hz confirms actual message flow and timing.
- ros2 doctor validates ROS environment health.
- ros2 param tools verify runtime configuration.
- Systematic debugging is faster and more reliable than modifying code without evidence.

---

## Engineering Reflection

### What is the first command you run when a ROS system appears broken?

ros2 node list

### Why is topic frequency important?

It confirms whether messages are being published at the expected rate and helps identify communication issues.

### What failures are easiest to diagnose?

Missing nodes and missing publishers because they are immediately visible through node and topic inspection tools.

### What failures are hardest to diagnose?

Incorrect parameter values and intermittent communication problems because the system may appear healthy while behaving incorrectly.

### How can systematic debugging save engineering time?

It isolates the root cause using evidence, preventing unnecessary code changes and reducing troubleshooting time.

---

## Completion Status

- Graph Inspection: Completed
- Topic Inspection: Completed
- Topic Diagnostics: Completed
- System Health Checks: Completed
- Parameter Verification: Completed
- Failure Injection: Completed
- Failure Diagnosis: Completed
- Recovery Procedure: Completed

Day 19 Status: COMPLETE