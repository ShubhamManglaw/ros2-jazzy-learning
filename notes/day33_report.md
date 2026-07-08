# 🖥️ Module 33 — RViz Visualization Engineering

## 🎯 Learning Goal

Understand how professional robotics engineers visualize, monitor, and debug ROS 2 systems using RViz.

By the end of this module, you should be able to:

- Visualize robot models
- Inspect TF trees
- Display sensor data
- Configure RViz professionally
- Debug robotics systems visually
- Integrate RViz into launch files

---

# Why RViz Exists

Robots continuously generate data:

- Lidar
- Cameras
- IMU
- Odometry
- TF transforms
- Navigation plans
- Maps
- Costmaps

Reading all this data from the terminal is inefficient.

RViz converts ROS data into visual information, allowing engineers to understand what the robot is doing in real time.

> **Engineering Rule:** If you cannot visualize your robot, debugging becomes dramatically harder.

---

# RViz Architecture

```
Robot
   │
   ▼
ROS Nodes
   │
   ▼
Topics + TF + Parameters
   │
   ▼
RViz Displays
   │
   ▼
Human Understanding
```

RViz is **not part of the robot's control system**.

It only subscribes to existing ROS data and renders it visually.

Closing RViz does **not** stop the robot.

---

# RViz Philosophy

RViz **does not create data**.

It only visualizes data published by other ROS nodes.

Sources include:

- Topics
- TF transforms
- Robot Description (URDF/Xacro)

---

# Display-Based Architecture

Everything in RViz is a **Display**.

Each display subscribes to a specific ROS interface.

| Display | Input | Purpose |
|----------|-------|----------|
| RobotModel | `robot_description` | Visualize URDF/Xacro robot |
| TF | `/tf`, `/tf_static` | Show coordinate frames |
| LaserScan | `/scan` | Visualize 2D lidar |
| PointCloud2 | `/points` | Visualize 3D sensors |
| Map | `/map` | Occupancy grid |
| Marker | `/visualization_marker` | Custom debugging objects |

---

# RobotModel Display

Purpose:

- Visualize URDF/Xacro robots

Requires:

```
robot_description
```

provided by

```
robot_state_publisher
```

---

# TF Display

Purpose:

Visualize coordinate frames.

Shows:

- Frame hierarchy
- Frame orientation
- Parent-child relationships

Essential for debugging transforms.

---

# LaserScan Display

Input:

```
sensor_msgs/LaserScan
```

Typically subscribes to:

```
/scan
```

Used to visualize 2D LiDAR.

---

# PointCloud2 Display

Used for:

- Depth cameras
- 3D LiDAR
- RGB-D cameras
- SLAM systems

Input:

```
sensor_msgs/PointCloud2
```

---

# Marker Display

Allows developers to draw custom objects for debugging.

Examples:

- Lines
- Arrows
- Cubes
- Spheres
- Text
- Axes

Common topic:

```
/visualization_marker
```

---

# Interactive Markers

Enable user interaction inside RViz.

Examples:

- Move robot goals
- Manipulate objects
- Interactive planning
- Robot control interfaces

---

# Fixed Frame

RViz requires a **Fixed Frame**.

Common choices:

```
map
```

```
odom
```

```
base_link
```

All visualized data is transformed into this frame using TF2.

Without valid TF transforms, displays will fail.

---

# Why TF2 is Critical

RViz depends heavily on TF2.

Without valid transforms:

- Robot model may disappear
- Sensors appear in the wrong location
- Navigation cannot be visualized correctly

---

# Navigation Visualization

RViz can display:

- Robot pose
- Global plan
- Local plan
- Costmaps
- Navigation goals
- Maps

Navigation2 provides dedicated RViz configurations.

---

# Manipulation Visualization

MoveIt uses RViz to visualize:

- Robot arms
- Collision objects
- Planning scene
- Motion plans
- End-effector goals

---

# RViz Configuration Files

Extension:

```
.rviz
```

Benefits:

- Repeatability
- Team consistency
- Faster startup
- Deployment simplicity

---

# Useful ROS Commands

Launch RViz

```bash
rviz2
```

Open configuration

```bash
rviz2 -d config.rviz
```

List topics

```bash
ros2 topic list
```

Inspect TF

```bash
ros2 topic echo /tf
```

Generate TF tree

```bash
ros2 run tf2_tools view_frames
```

View robot description

```bash
ros2 param get /robot_state_publisher robot_description
```

Inspect LaserScan

```bash
ros2 topic echo /scan
```

---

# Typical Engineering Workflow

1. Launch Robot State Publisher
2. Launch Joint State Publisher
3. Launch RViz
4. Set Fixed Frame
5. Add RobotModel
6. Add TF Display
7. Add Sensor Displays
8. Save `.rviz`
9. Integrate into launch file

---

# Package Structure

```
my_robot_description/

├── urdf/
├── launch/
├── rviz/
│   └── robot.rviz
├── config/
├── package.xml
└── CMakeLists.txt
```

---

# Common Debugging Problems

## Robot Not Visible

Cause

```
robot_description missing
```

Fix

Verify:

```
robot_state_publisher
```

---

## TF Errors

Cause

```
Missing transforms
```

Fix

Inspect:

```
/tf
```

or

```bash
ros2 run tf2_tools view_frames
```

---

## Laser Not Visible

Possible causes

- Wrong topic
- Wrong Fixed Frame
- Missing TF
- Display disabled

---

## Point Cloud Missing

Possible causes

- TF mismatch
- Wrong topic
- Sensor not publishing

---

## RViz Crash

Possible causes

- Invalid configuration
- Corrupted `.rviz`
- Graphics driver issues

---

# Debugging Checklist

```bash
ros2 node list
```

```bash
ros2 topic list
```

```bash
ros2 topic echo /tf
```

```bash
ros2 param get /robot_state_publisher robot_description
```

Check:

- Fixed Frame
- Display Topics
- TF Tree
- RViz logs

---

# Deliverables

- Robot visualization
- TF visualization
- Laser visualization
- Point cloud visualization
- Marker visualization
- Saved `.rviz` configuration
- Launch integration

---

# Key Takeaways

- RViz is ROS 2's primary visualization tool.
- RViz only visualizes data; it never creates it.
- Every display subscribes to a ROS topic or interface.
- RobotModel depends on `robot_description`.
- TF2 is fundamental for correct visualization.
- Fixed Frame determines the reference frame for all displays.
- `.rviz` files make visualization reproducible.
- RViz is one of the most important debugging tools in professional robotics.
