Day 30 Report — URDF Engineering

Objective

Learn the fundamentals of URDF (Unified Robot Description Format) and understand how robot models are represented, connected, and published into the ROS 2 TF ecosystem.

⸻

Work Completed

1. Created Robot Description Package

Created the package:

my_robot_description

Organized the package using the standard ROS robot description structure:

my_robot_description/
├── launch/
├── rviz/
├── urdf/
├── package.xml
└── setup.py

⸻

2. Built First URDF Model

Created the robot:

<robot name="newton_bot">

Added the primary robot body:

<link name="base_link">

Represented the chassis using box geometry:

<box size="0.2 0.15 0.1"/>

⸻

3. Integrated robot_state_publisher

Created a launch file that:

1. Loads the URDF file.
2. Reads the file contents.
3. Publishes the contents as the robot_description parameter.
4. Starts robot_state_publisher.

Architecture:

my_robot.urdf
        ↓
robot_description
        ↓
robot_state_publisher
        ↓
TF

Verified successful parameter loading using:

ros2 param get /robot_state_publisher robot_description

⸻

4. Added Additional Links

Added:

camera_link
lidar_link

Resulting robot structure:

base_link
├── camera_link
└── lidar_link

⸻

5. Added Fixed Joints

Created:

camera_joint
lidar_joint

Connected child links to the base frame:

<parent link="base_link"/>
<child link="camera_link"/>

and

<parent link="base_link"/>
<child link="lidar_link"/>

⸻

6. Defined Relative Origins

Camera position:

<origin xyz="0 0 0.05"/>

Lidar position:

<origin xyz="0 0 0.08"/>

Learned that joint origins define the pose of the child frame relative to the parent frame.

⸻

7. Generated TF Tree from URDF

Verified automatic TF generation through robot_state_publisher.

Observed transforms:

base_link → camera_link
base_link → lidar_link

Verified using:

ros2 topic echo /tf_static --once

⸻

8. Visualized TF Architecture

Generated TF tree using:

ros2 run tf2_tools view_frames

Result:

base_link
├── camera_link
└── lidar_link

Successfully exported and inspected the generated PDF frame graph.

⸻

9. Integrated RViz

Added RViz to the launch system.

Verified:

RobotModel: OK
TF: OK
Fixed Frame: base_link

Confirmed successful RobotModel loading from the robot_description parameter.

⸻

Concepts Learned

Link

A rigid body in the robot model.

Examples:

base_link
camera_link
lidar_link

⸻

Joint

Defines the relationship between two links.

Example:

base_link
    │
camera_joint
    │
camera_link

⸻

Origin

Defines the position and orientation of the child frame relative to the parent frame.

<origin xyz="0 0 0.05"/>

⸻

robot_state_publisher

Converts a URDF robot model into a TF tree and publishes transforms automatically.

⸻

URDF → TF Pipeline

URDF
  ↓
robot_description
  ↓
robot_state_publisher
  ↓
TF Tree
  ↓
RViz

⸻

Final Robot Architecture

base_link
├── camera_link
└── lidar_link

Generated through:

2 Links
+ 2 Fixed Joints
+ 2 Origins

⸻

Key Takeaways

1. URDF describes robot structure using links and joints.
2. Links represent rigid bodies.
3. Joints define relationships between bodies.
4. Origins define relative poses.
5. robot_state_publisher converts URDF into TF frames.
6. TF trees can be inspected using tf2_tools and RViz.
7. Robot models are distributed through the robot_description parameter.

⸻

Day 30 Status

Module 30 objectives completed successfully.

Completion Estimate: 95%

Next Module: Xacro Engineering