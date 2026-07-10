# Module 34 — Parameter Architecture Engineering
## Day 34 Report

**Date:** ____________

**Module:** 34

**Status:** ✅ Completed

**Workspace:** `ros2-jazzy-learning`

**Package:** `ros2_advanced`

---

# Objectives

This module focused on moving beyond the basic ROS 2 Parameter API and understanding how professional robotics software manages configuration safely and at scale.

Rather than revisiting parameter fundamentals, the emphasis was on engineering practices used in production robotics systems.

---

# Topics Covered

## 1. Parameter Architecture

Learned the difference between:

- Software Logic
- Configuration

Key principle:

> **Code describes behavior. Parameters describe configuration.**

Understood why robots should never hardcode configurable values.

Examples:

- Joint limits
- Controller gains
- Camera settings
- Planning parameters
- Robot dimensions

---

## 2. Configuration Engineering

Discussed why large robots never use one huge YAML file.

Instead configuration should be separated by responsibility.

Example:

```text
config/
├── camera.yaml
├── controllers.yaml
├── gripper.yaml
├── joint_limits.yaml
├── moveit.yaml
├── planning.yaml
├── ros2_control.yaml
├── sensors.yaml
├── simulation.yaml
└── visualization.yaml
```

Benefits:

- Easier debugging
- Clear ownership
- Better Git history
- Better scalability
- Easier maintenance

---

# Practical Implementation

## Created Advanced Learning Package

Workspace:

```text
~/ros2-jazzy-learning
```

Created package:

```text
ros2_advanced
```

Package structure:

```text
ros2_advanced/
├── config/
├── launch/
├── package.xml
├── resource/
├── setup.py
├── setup.cfg
├── test/
└── ros2_advanced/
    ├── __init__.py
    └── nodes/
        └── parameters/
            ├── __init__.py
            ├── descriptor_node.py
            └── validation_node.py
```

This package will continue to grow throughout future advanced ROS 2 modules.

---

# setup.py Improvements

Updated package installation to include:

- Launch files
- Configuration files

using:

```python
glob()
os.path.join()
```

Also registered console scripts correctly.

---

# Lesson 1 — Parameter Descriptors

## Purpose

Parameter descriptors provide metadata about parameters.

Instead of only storing a value, ROS can also describe:

- Description
- Units
- Constraints
- Read-only status

Used:

```python
ParameterDescriptor
```

Example:

```python
descriptor = ParameterDescriptor(
    description="Maximum joint velocity in rad/s"
)

self.declare_parameter(
    "max_velocity",
    1.0,
    descriptor
)
```

Verified using:

```bash
ros2 param describe
```

---

# Lesson 2 — Parameter Validation Callbacks

Implemented:

```python
add_on_set_parameters_callback()
```

Created validation callback using:

```python
SetParametersResult
```

Validation logic:

- Reject velocity ≤ 0
- Reject velocity > 10

Accepted values:

```
0 < velocity ≤ 10
```

Returned informative error messages when validation failed.

---

# Dynamic Runtime Parameters

Verified runtime updates using:

```bash
ros2 param set
```

Example:

```bash
ros2 param set /validation_node max_velocity 5.0
```

Observed runtime log:

```text
Maximum velocity updated to 5.0
```

Invalid example:

```bash
ros2 param set /validation_node max_velocity -5
```

ROS correctly responded:

```text
Setting parameter failed

Maximum velocity must be between 0 and 10
```

---

# Development Workflow

Standard workflow adopted:

```bash
cd ~/ros2-jazzy-learning

colcon build --packages-select ros2_advanced --symlink-install

source install/setup.bash
```

Learned why `--symlink-install` is preferred for Python development.

---

# Engineering Principles Learned

## Parameter Descriptor

Purpose:

- Documentation
- Discoverability
- Better tooling

Does **not** validate parameters.

---

## Validation Callback

Purpose:

- Safety
- Configuration validation

Does **not** update parameters.

ROS updates the parameter automatically after successful validation.

---

## Dynamic Parameters

Allow runtime configuration changes without restarting the node.

Suitable for:

- PID gains
- Camera exposure
- Logging level
- Planner timeout
- Speed limits

---

## Configuration Best Practices

Parameters should represent values that differ between:

- Robots
- Environments
- Deployments

Do **not** expose constants as parameters.

Examples that should NOT be parameters:

- π
- Gravity constant
- Fixed algorithm constants

---

## Configuration Ownership

Configuration should be grouped by subsystem responsibility.

Examples:

- Camera → `camera.yaml`
- MoveIt → `moveit.yaml`
- Controller → `controllers.yaml`
- ros2_control → `ros2_control.yaml`

---

# Files Created

```text
ros2_advanced/
└── ros2_advanced/
    └── nodes/
        └── parameters/
            ├── descriptor_node.py
            └── validation_node.py
```

---

# Commands Practiced

```bash
ros2 run ros2_advanced descriptor_node

ros2 run ros2_advanced validation_node

ros2 param list

ros2 param get

ros2 param set

ros2 param describe
```

---

# Debugging Lessons

Learned to diagnose:

- Missing console scripts
- Incorrect `setup.py`
- Missing `__init__.py`
- Incorrect imports
- Callback registration
- Package installation issues
- Difference between validation and parameter updates

---

# Key Engineering Takeaways

- Configuration should be separated from implementation.
- Parameters should be documented using descriptors.
- Invalid parameter values must be rejected.
- Runtime updates improve robot tuning without restarts.
- Configuration files should be organized by subsystem.
- Python ROS 2 packages should use `--symlink-install` during development.
- Validation callbacks are used throughout production robotics software.

---

# Skills Gained

- ROS 2 Parameter Engineering
- Configuration Architecture
- Parameter Descriptors
- Validation Callbacks
- Dynamic Runtime Parameters
- Python ROS 2 Package Organization
- Professional Debugging Workflow

---

# Module Completion

| Topic | Status |
|--------|--------|
| Parameter Fundamentals | ✅ |
| YAML Configuration | ✅ |
| Launch Integration | ✅ |
| Parameter Architecture | ✅ |
| Parameter Descriptors | ✅ |
| Validation Callbacks | ✅ |
| Dynamic Parameters | ✅ |
| Production Best Practices | ✅ |

---

# Overall Assessment

Module 34 established the software engineering practices required for building configurable, maintainable, and production-ready ROS 2 systems.

The concepts learned here will be directly reused in:

- 6-DOF Robotic Arm
- AUV Software Stack
- MoveIt 2
- ros2_control
- Navigation Systems

---

# Next Module

## Module 35 — ROS 2 Workspace & Package Architecture Engineering

Focus:

- Workspace organization
- Package responsibilities
- Dependency management
- Multi-package robotics architectures
- Production ROS repository design
```