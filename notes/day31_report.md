# Day 31 Report — Xacro Engineering

## Objective

Convert a monolithic URDF into a modular, reusable Xacro project suitable for professional ROS 2 development.

---

# Learning Outcomes

Completed:

- Xacro introduction
- Properties
- Includes
- Macros
- Parameterized macros
- Modular robot architecture
- Base macro
- Wheel macro
- Material definitions
- Camera sensor
- URDF generation
- URDF validation
- TF verification

---

# Final Package Structure

```
my_robot_description/
│
├── launch/
│   └── display.launch.py
│
├── rviz/
│
├── urdf/
│   ├── robot.urdf.xacro
│   ├── base.xacro
│   ├── wheels.xacro
│   ├── materials.xacro
│   ├── sensors.xacro
│   └── robot.urdf
│
├── package.xml
└── CMakeLists.txt
```

---

# Xacro Architecture

```
robot.urdf.xacro
        │
        ├── base.xacro
        ├── wheels.xacro
        ├── sensors.xacro
        └── materials.xacro
```

The top-level file assembles the robot.

Each component is defined independently.

---

# Concepts Learned

## xacro:property

Used as reusable global variables.

Example:

- wheel_radius
- wheel_width
- robot_length
- robot_width

---

## xacro:include

Used to split robot description across multiple files.

Benefits:

- Cleaner architecture
- Easier debugging
- Better maintainability
- Reusability

---

## xacro:macro

Equivalent to reusable functions.

Example:

```
<xacro:wheel
    name="front_left_wheel"
    parent="base_link"
    x="0.2"
    y="0.2"/>
```

The macro generates:

- Link
- Joint

automatically.

---

# Robot Components

## Base

- base_link
- Visual
- Collision
- Inertial

---

## Wheels

Implemented as parameterized macro.

Inputs:

- name
- parent
- x
- y

Outputs:

- Wheel Link
- Wheel Joint

---

## Materials

Reusable colors:

- Black
- Blue
- Red
- White

---

## Sensors

Added:

- Camera

Connected using:

```
camera_joint
```

---

# Commands Used

Generate URDF

```
xacro robot.urdf.xacro -o robot.urdf
```

Validate URDF

```
check_urdf robot.urdf
```

Visualize

```
ros2 launch my_robot_description display.launch.py
```

Generate TF Tree

```
ros2 run tf2_tools view_frames
```

---

# Debugging Performed

## Duplicate Link Error

Error:

```
link 'front_left_wheel' is not unique
```

Cause:

Wheel was manually defined and also generated through macro.

Fix:

Removed manual wheel definition.

---

## Missing Packages

Installed:

```
ros-jazzy-joint-state-publisher
ros-jazzy-joint-state-publisher-gui
ros-jazzy-rviz2
```

---

# Verification

Passed:

- Xacro generation
- URDF validation
- TF Tree generation
- Robot State Publisher

Verified Frames:

- base_link
- front_left_wheel
- front_right_wheel
- rear_left_wheel
- rear_right_wheel
- camera_link

---

# Key Engineering Lessons

- Xacro is a preprocessor, not a robot description format.
- Macros eliminate duplicated URDF.
- Properties provide a single source of truth.
- Includes improve maintainability.
- Joints define the robot's kinematic tree.
- Robot descriptions should be modular.

---

# Module Progress

Module 31 Completion:

**≈95%**

Completed:

- Modular Xacro
- Robot assembly
- Validation
- TF verification

Pending:

- Final RViz rendering issue (likely environment/configuration related, not Xacro).

---

# Next Module

Module 32

Robot State Publisher Engineering

Focus:

- Robot Description parameter
- Joint State Publisher
- TF broadcasting
- RViz visualization
- Launch architecture