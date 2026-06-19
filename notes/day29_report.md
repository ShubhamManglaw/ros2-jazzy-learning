Day 29 Report — TF2 Coordinate Frames Engineering

Objective

Learn how robots represent spatial relationships using TF2, build static and dynamic transform systems, visualize frame trees, and create both transform broadcasters and listeners.

⸻

Work Completed

1. Static Transform Fundamentals

Explored ROS 2 TF2 tooling and verified available utilities:

* tf2_echo
* static_transform_publisher
* tf2_monitor
* view_frames

Verified that no TF system existed initially:

ros2 topic list

Observed absence of:

/tf
/tf_static

which demonstrated that no transform broadcasters were active.

⸻

2. Static Transform Publishing

Created a static transform between:

base_link
    │
    ▼
camera_link

using:

ros2 run tf2_ros static_transform_publisher \
--x 0.2 \
--y 0.0 \
--z 0.0 \
--frame-id base_link \
--child-frame-id camera_link

Verified publication through:

ros2 topic echo /tf_static

and confirmed:

frame_id: base_link
child_frame_id: camera_link

with a translation of 0.2 meters.

⸻

3. TF Querying

Used:

ros2 run tf2_ros tf2_echo base_link camera_link

to query the transform.

Verified:

Translation: [0.200, 0.000, 0.000]

and observed how TF2 resolves frame relationships.

⸻

4. Building a Frame Tree

Created a second static transform:

base_link
    │
    ├── camera_link
    └── lidar_link

using an additional static transform publisher.

Generated and inspected the frame graph with:

ros2 run tf2_tools view_frames

Successfully visualized the frame hierarchy and exported the generated PDF graph.

⸻

5. Dynamic Transform Broadcaster

Created a new package:

tf2_demo

and implemented a custom TF broadcaster node.

Core components used:

* TransformBroadcaster
* TransformStamped
* Timer callback

Published the dynamic transform:

odom
   │
   ▼
base_link

through:

self.tf_broadcaster.sendTransform(transform)

Verified appearance of:

/tf

and inspected messages using:

ros2 topic echo /tf

⸻

6. Simulated Robot Motion

Enhanced the broadcaster to continuously update position.

Implemented:

self.x += 0.1

inside the timer callback.

Observed transform updates:

odom → base_link

with increasing X coordinates over time.

Verified using:

ros2 run tf2_ros tf2_echo odom base_link

Example output:

Translation:
11.8
12.8
13.8
14.8

demonstrating dynamic robot motion.

⸻

7. TF Listener

Implemented a dedicated TF listener node.

Core components:

* Buffer
* TransformListener
* lookup_transform()

Queried:

odom → base_link

from the TF buffer.

Successfully retrieved and logged robot position values:

x = 6.8
x = 7.8
x = 8.8
...

confirming end-to-end TF communication.

⸻

8. Robustness Improvements

Added:

TransformException

handling to avoid listener failures when transforms are temporarily unavailable.

This mirrors production-grade TF listener behavior.

⸻

9. Launch Integration

Created:

launch/tf_demo.launch.py

to start:

* dynamic_broadcaster
* tf_listener

simultaneously.

Verified successful launch:

ros2 launch tf2_demo tf_demo.launch.py

Observed:

/dynamic_broadcaster
/tf_listener

and continuous transform updates.

⸻

Key Concepts Learned

Static TF

Used for fixed robot components:

base_link
 ├── camera_link
 └── lidar_link

Published on:

/tf_static

⸻

Dynamic TF

Used for moving coordinate frames:

odom
   │
   ▼
base_link

Published on:

/tf

⸻

TF Architecture

TransformBroadcaster
        ↓
       /tf
        ↓
TransformListener
        ↓
      Buffer
        ↓
lookup_transform()

⸻

Final Result

Successfully built a complete TF2 workflow consisting of:

* Static transform publishers
* Dynamic transform broadcaster
* TF listener
* Frame tree visualization
* TF querying tools
* Launch integration
* Exception handling

The system continuously publishes and consumes transforms, providing a simplified simulation of how localization and navigation systems exchange coordinate frame information in a real robot.

Module Status

Module 29 Complete