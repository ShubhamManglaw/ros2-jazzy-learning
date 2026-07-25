Day 39 Report — Simulation & Digital Twin Engineering

Date: July 25, 2026

Module: 39 — Simulation & Digital Twin Engineering

Status: ✅ Completed

⸻

Objective

The objective of this module was to understand how robotic simulation works in professional ROS 2 systems and to build the first complete simulation pipeline for the project robot. Unlike earlier URDF-only work, the goal here was not just to visualize a robot, but to make it behave like a real ROS 2 robotic system inside Gazebo.

This module focused on simulation architecture, Gazebo integration, ROS 2 bridging, motion, odometry, TF, and simulated sensing.

⸻

Topics Covered

1. Why Robotics Simulation Exists

Learned why simulation is essential in modern robotics engineering.

Studied how simulation helps reduce:

* hardware cost
* risk of damage
* debugging time
* iteration time

Key takeaway:

Simulation allows engineers to test robot behavior, software, and system architecture before deploying to real hardware.

⸻

2. Digital Twins

Understood the difference between:

* a simulation
* a simulator
* a digital twin

Learned that a digital twin is not just a robot model in a simulator. It is a virtual representation of a real robot or system that can reflect and support real-world behavior, monitoring, and validation.

Key takeaway:

Simulation is used for development and testing. Digital twins extend this idea into lifecycle support, monitoring, and system-level reasoning.

⸻

3. Gazebo Architecture

Studied the core components of Gazebo Harmonic.

Covered:

* world
* model
* link
* joint
* plugin
* sensor
* transport topics

Important understanding:

Gazebo is not just a viewer. It is a simulation environment made of multiple interacting systems.

Key takeaway:

A robot in Gazebo only works properly when the robot description, the world, the plugins, and the simulation systems are all configured correctly.

⸻

4. Gazebo Installation and Basic Interaction

Confirmed that Gazebo Harmonic and `ros_gz` packages were installed and working in the ROS 2 Jazzy environment.

Learned to:

* launch Gazebo
* inspect available models and worlds
* use the empty world
* insert basic objects
* observe gravity and collisions

Key takeaway:

Before simulating a robot, the simulator itself must be validated with simple objects and known behavior.

⸻

5. Spawning a Robot from URDF/Xacro

Connected the earlier URDF/Xacro work to Gazebo for the first time.

Built an initial launch architecture using:

* `robot_state_publisher`
* `ros_gz_sim`
* `ros_gz_bridge`
* `rviz2`

Used `robot_description` and `ros_gz_sim create` to spawn the robot into Gazebo.

Key takeaway:

Gazebo does not magically know the robot. ROS 2 must provide the robot description and explicitly request spawning.

⸻

6. Gazebo-Specific Robot Configuration

Created `gazebo.xacro` to keep simulator-specific configuration separate from the core robot geometry.

Added:

* visual Gazebo material
* DiffDrive plugin
* LiDAR sensor configuration

Important architectural lesson:

The robot description should define the robot. Gazebo-specific behavior should be isolated in Gazebo-specific files.

⸻

7. Differential Drive Simulation

Added and configured the Gazebo Harmonic DiffDrive system for the four-wheel robot.

Configured:

* left wheel joints
* right wheel joints
* wheel radius
* wheel separation
* odometry topic
* base and odom frame relationship

Initially encountered incorrect motion behavior where the robot flipped or moved sideways instead of driving correctly.

Diagnosed and fixed:

* wheel joint axis issues
* robot geometry assumptions
* rebuild and install synchronization issues

Final result:

The robot moved correctly using differential drive commands.

⸻

8. ROS 2 ↔ Gazebo Bridge

Studied why ROS 2 and Gazebo cannot communicate directly by default.

Learned that:

* ROS 2 uses DDS
* Gazebo uses Gazebo Transport
* `ros_gz_bridge` translates between them

Bridged the following topics:

* `/cmd_vel`
* `/odom`
* `/clock`
* `/tf`
* `/scan`

Important debugging lesson:

A topic name existing in both ROS 2 and Gazebo does not mean data is flowing. Each layer must be verified independently.

⸻

9. Time, Odometry, and TF

Configured and verified simulation-time behavior.

Fixed `use_sim_time` after diagnosing that the edited launch file had not been saved before rebuild.

Verified:

* `/clock`
* `/odom`
* dynamic TF from `odom` to `base_link`

Used:

* `ros2 param get`
* `ros2 topic echo`
* `ros2 run tf2_ros tf2_echo odom base_link`

Key takeaway:

A simulated robot is only useful if time, odometry, and transforms are consistent across the full ROS graph.

⸻

10. Teleoperation and Motion Verification

Confirmed that the robot could be driven using keyboard teleoperation.

Verified:

* forward motion
* rotational motion
* stop commands
* changing odometry values
* changing TF values

Important lesson:

When debugging robot movement, it is necessary to separate:

* command generation
* bridge behavior
* plugin behavior
* robot mechanics
* world physics

⸻

11. LiDAR Sensor Integration

Added a physical `lidar_link` to the robot description and mounted it above the robot body.

Then added a Gazebo LiDAR sensor attached to that link.

Important issue encountered:

The LiDAR topic name appeared in Gazebo before real data flowed, which initially made the system look partially correct even though the sensor was not fully active.

Resolved by:

* completing the LiDAR sensor definition
* creating a custom world file with the Gazebo sensors system enabled
* installing the `worlds/` directory properly through `setup.py`

Verified:

* Gazebo publishes `/scan`
* ROS 2 receives `/scan`
* `sensor_msgs/msg/LaserScan` contains both infinite values and finite obstacle distances

Key takeaway:

Robot-mounted sensors belong in the robot description, but simulation systems that activate them belong in the world configuration.

⸻

12. Package Installation and Runtime Debugging

Encountered several runtime issues caused by differences between source files and installed package files.

Important problems diagnosed during the module:

* forgetting to rebuild after changing Xacro
* forgetting to source the workspace after rebuild
* unsaved launch-file edits
* world file not being installed because `setup.py` did not include `worlds/`
* duplicate running bridge nodes causing confusing topic behavior

Key takeaway:

In ROS 2, runtime behavior depends on the installed package, not just the source tree.

⸻

Final Working System

By the end of Day 39, the project robot successfully included:

* modular Xacro-based robot description
* Gazebo Harmonic simulation world
* robot spawning through ROS 2
* differential drive motion
* keyboard teleoperation
* bridged `/cmd_vel`
* bridged `/odom`
* bridged `/clock`
* bridged dynamic TF
* mounted LiDAR sensor
* bridged `/scan` topic into ROS 2

This is now a complete simulated mobile robot pipeline, not just a static visual model.

⸻

Major Engineering Lessons

1. Robot description and world configuration are different layers

The robot file should describe:

* robot structure
* mounted hardware
* joints
* links
* robot-specific plugins

The world file should describe:

* simulation environment
* global simulation systems
* physics systems
* sensor system plugins

⸻

2. Topic registration is not the same as topic flow

A topic can exist in:

* Gazebo
* ROS 2
* the bridge

without actual message flow being correct.

Every layer must be verified directly.

⸻

3. Source and install mismatch is a real robotics debugging issue

Many issues were not caused by incorrect concepts, but by:

* stale installed files
* missing asset installation
* unsourced workspace changes

⸻

4. Gazebo and ROS 2 must be debugged as a system

Reliable debugging required checking:

1. Xacro/URDF generation
2. package installation
3. Gazebo world loading
4. robot spawning
5. Gazebo topic publishing
6. bridge behavior
7. ROS 2 topic flow

⸻

Outcome

Module 39 successfully transformed the project from:

* a URDF/Xacro robot description that could be visualized

into:

* a ROS 2 simulated mobile robot that can move, publish odometry, maintain TF, and produce LiDAR scan data

This establishes the correct foundation for moving beyond robot description into robot control architecture.

⸻

Next Module

Module 40 — ROS 2 Control and Hardware Abstraction

The next phase should focus on how simulated and physical robots are controlled through a structured controller architecture rather than only through simulator plugins.
