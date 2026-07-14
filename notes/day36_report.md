# Module 36 — Multi-Robot Systems Engineering
## Day 36 Report

**Date:** ____________

**Module:** 36

**Status:** ✅ Completed

**Workspace:** `ros2-jazzy-learning`

---

# Module Objective

The objective of this module was to understand how ROS 2 scales from a single robot to multiple robots using namespaces, launch architecture, and distributed communication principles.

Unlike previous modules that focused on software architecture inside one robot, this module introduced the engineering concepts required to deploy multiple independent robot instances using the same codebase.

The primary emphasis was on writing reusable, namespace-aware ROS 2 software instead of duplicating code for each robot.

---

# Topics Covered

## 1. Multi-Robot System Fundamentals

Learned why modern robotics increasingly relies on multiple robots working together.

Examples discussed:

- Warehouse robots
- Factory robotic arms
- Drone swarms
- Autonomous vehicle fleets
- Underwater robot teams

Studied why ROS 2 was designed for distributed robotics rather than single-robot applications.

---

# Why Multi-Robot Architecture Matters

Without proper isolation:

- Topic collisions
- TF conflicts
- Service conflicts
- Action conflicts
- Difficult debugging

ROS 2 solves these problems through namespaces and distributed deployment.

---

# Namespaces

Studied the purpose of namespaces.

Example:

```text
Robot 1

/arm1/status
/arm1/joint_states

Robot 2

/arm2/status
/arm2/joint_states
```

Each robot owns its own namespace.

The same executable can therefore run multiple independent robot instances.

---

# Relative vs Absolute Names

Learned the difference between:

Relative:

```python
"status"
```

Absolute:

```python
"/status"
```

Relative names automatically inherit the robot namespace.

Absolute names ignore namespaces and therefore should not be used for robot-specific topics.

Engineering rule:

Robot-specific topics should almost always use relative names.

---

# Namespace Demonstration

Created package:

```text
namespace_demo
```

Implemented:

```text
status_publisher.py
```

Node functionality:

- Publisher
- Timer
- String messages
- Status logging

Published:

```text
status
```

using a relative topic name.

---

# Multi-Robot Deployment

Launched multiple instances of the same executable.

Example:

```bash
ros2 run namespace_demo status_publisher --ros-args -r __ns:=/arm1

ros2 run namespace_demo status_publisher --ros-args -r __ns:=/arm2
```

Verified that no Python code changes were required.

Deployment alone determined robot identity.

---

# Launch Architecture

Created:

```text
launch/
└── multi_robot.launch.py
```

Launch file deployed two robot instances.

Example architecture:

```python
Node(
    package="namespace_demo",
    executable="status_publisher",
    namespace="arm1"
)

Node(
    package="namespace_demo",
    executable="status_publisher",
    namespace="arm2"
)
```

This demonstrated how professional ROS 2 systems launch multiple robots from a single launch file.

---

# Setup.py Configuration

Configured launch file installation.

Added:

```python
(os.path.join('share', package_name, 'launch'),
 glob('launch/*.launch.py'))
```

This allows ROS 2 to locate launch files after installation.

---

# Verification

Verified nodes:

```text
/arm1/status_publisher
/arm2/status_publisher
```

Verified topics:

```text
/arm1/status
/arm2/status
```

Observed successful namespace isolation.

---

# Launch Philosophy

Learned separation between:

Behavior

↓

Node implementation

Deployment

↓

Launch system

Configuration

↓

Parameters + namespaces

The node itself never knows whether it belongs to:

```text
/arm1
```

or

```text
/arm2
```

Deployment decides.

---

# TF Isolation

Studied why each robot requires an independent TF tree.

Incorrect:

```text
base_link
tool0
```

published by every robot.

Correct:

```text
arm1/base_link
arm1/tool0

arm2/base_link
arm2/tool0
```

This prevents frame collisions.

---

# Shared vs Private Topics

Private topics:

```text
/arm1/status
/arm1/joint_states
```

Shared topics:

```text
/clock
/map
/emergency_stop
```

Engineering rule:

Robot-specific information belongs inside namespaces.

System-wide information remains global.

---

# Robot-Specific Parameters

Learned that identical robots may require different configurations.

Example:

```yaml
arm1.yaml

max_velocity: 1.0
```

```yaml
arm2.yaml

max_velocity: 0.5
```

The same node loads different parameter files depending on deployment.

---

# Fleet Architecture

Studied how ROS 2 scales.

One robot:

```text
Arm1
```

↓

Many robots:

```text
Arm1
Arm2
Arm3
...
Arm100
```

Still using:

- One executable
- One codebase
- One launch architecture

Only namespaces and parameter files change.

---

# Common Multi-Robot Mistakes

Identified common beginner mistakes.

- Hardcoded namespaces
- Absolute topic names
- Duplicate controller implementations
- Shared TF frames
- Shared parameter files

Professional ROS 2 systems avoid these patterns.

---

# Practical Skills Acquired

Implemented:

- Namespace-aware publisher
- Multi-robot launch file
- Launch directory
- Launch installation in setup.py

Verified:

- Namespace isolation
- Topic isolation
- Node isolation

Used:

- ros2 run
- ros2 launch
- ros2 node list
- ros2 topic list

---

# Engineering Principles Learned

- One executable can support many robots.
- Deployment belongs in launch files.
- Behavior belongs in nodes.
- Relative topic names support scalability.
- Namespaces isolate robot resources.
- TF trees must remain independent.
- Parameters should be robot-specific.
- Scale systems through configuration rather than duplicated code.

---

# Skills Gained

- ROS 2 Namespaces
- Multi-Robot Deployment
- Launch Architecture
- Topic Isolation
- Node Isolation
- TF Isolation Concepts
- Fleet Software Design
- Distributed ROS 2 Systems
- Namespace Debugging

---

# Module Completion Checklist

| Topic | Status |
|--------|--------|
| Multi-Robot Fundamentals | ✅ |
| ROS 2 Namespaces | ✅ |
| Relative vs Absolute Names | ✅ |
| Namespace-Aware Nodes | ✅ |
| Launch Architecture | ✅ |
| Multi-Robot Launch Files | ✅ |
| Topic Isolation | ✅ |
| Node Isolation | ✅ |
| TF Isolation | ✅ |
| Shared vs Private Topics | ✅ |
| Robot-Specific Parameters | ✅ |
| Fleet Architecture | ✅ |
| Common Multi-Robot Mistakes | ✅ |

---

# Overall Assessment

Module 36 introduced the engineering concepts required to scale ROS 2 applications from a single robot to many robots without modifying application code.

The practical implementation demonstrated how namespaces, launch files, and deployment configuration allow one executable to represent multiple independent robots.

These concepts form the foundation for fleet robotics, distributed systems, collaborative robots, and scalable ROS 2 software engineering.

---

# Next Module

## Module 37 — DDS & Middleware Engineering

Focus:

- DDS Discovery
- Middleware Architecture
- QoS Policies
- Reliability vs Best Effort
- Communication Performance
- DDS Debugging
- ROS 2 Communication Internals