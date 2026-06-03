# Day 03 Report – Publisher Internals

## Date

June 2026

## Objective

Understand how ROS 2 publishers work internally and build a custom publisher node without copying tutorial code.

## Concepts Covered

### Publisher Architecture

Node
→ Publisher
→ Topic
→ Subscriber

### Publisher Creation

create_publisher()

Parameters:

* Message Type
* Topic Name
* Queue Depth

### Queue Depth

Controls how many messages can be buffered if communication temporarily falls behind.

### Timer Callbacks

create_timer()

Used for periodic execution.

Learned the difference between:

self.publish_distance

and

self.publish_distance()

### Node State

Using:

self.distance

to maintain state across callback executions.

### Message Publishing

Message Object
→ Populate Data
→ Publish
→ Subscriber Receives

### ROS Topic Inspection

* ros2 topic list
* ros2 topic info
* ros2 topic echo
* ros2 topic hz

## Practical Project

Built a custom sensor simulator:

DistancePublisher

### Topic

ultrasonic_distance

### Message Type

String

### Publishing Rate

1 Hz

### Simulated Data

120 cm
119 cm
118 cm
...
0 cm

### Logic Implemented

* Create publisher
* Create timer
* Generate message
* Publish message
* Decrease distance
* Stop at zero

## Debugging Experience

### Package Not Found

Cause:

Workspace not sourced.

Fix:

source install/setup.bash

### Missing Executable

Cause:

Incorrect setup.py entry-point configuration.

Fix:

Updated console_scripts and rebuilt package.

### Executable Verification

Used:

```bash
ros2 pkg executables my_first_pkg
```

to verify installation.

## Commands Practiced

```bash
ros2 run my_first_pkg distance_publisher

ros2 topic list

ros2 topic info /ultrasonic_distance

ros2 topic echo /ultrasonic_distance

ros2 topic hz /ultrasonic_distance

ros2 pkg executables my_first_pkg
```

## Key Learnings

* Publishers are objects returned by create_publisher().
* Callbacks must be passed as references.
* State should be stored using self variables.
* Queue depth acts as a message buffer.
* setup.py controls ROS executables.
* rclpy.spin() keeps callbacks alive.
* Publishing is different from printing.

## Outcome

Can independently design, implement, register, build, run, and debug a custom ROS 2 publisher node. Understand publisher lifecycle, timer callbacks, state management, package registration, and ROS topic inspection tools.
