Day 25 Report — Lifecycle Nodes Engineering

Completion Date

2026-06-15

⸻

Objective

Learn and implement ROS 2 Lifecycle Nodes to build deterministic startup, activation, deactivation, cleanup, shutdown, and lifecycle orchestration behavior similar to production robotics systems such as Navigation2.

⸻

Packages Created

lifecycle_demo

Implemented:

* Lifecycle Node
* Lifecycle Publisher
* Timer-based publisher
* Lifecycle Manager

⸻

Lifecycle Node Implementation

Created a custom Lifecycle Node using:

LifecycleNode

Implemented lifecycle callbacks:

* on_configure()
* on_activate()
* on_deactivate()
* on_cleanup()
* on_shutdown()
* on_error()

⸻

Resource Management

Resources are allocated during configuration:

* LifecyclePublisher
* Timer

Resources are released during cleanup:

* Publisher reference cleared
* Timer destroyed
* Timer reference cleared

Implemented defensive callback protection to prevent publishing after cleanup.

⸻

Lifecycle Publisher Verification

Created:

self.create_lifecycle_publisher(...)

Verified behavior:

Inactive State

Messages are not published.

Active State

Messages are published successfully.

Deactivated State

Publishing stops immediately.

This verified LifecyclePublisher state enforcement.

⸻

Lifecycle State Verification

Verified transitions:

Unconfigured
    ↓
Configure
    ↓
Inactive
    ↓
Activate
    ↓
Active
    ↓
Deactivate
    ↓
Inactive
    ↓
Cleanup
    ↓
Unconfigured

Verified using:

ros2 lifecycle get /lifecycle_node
ros2 lifecycle set /lifecycle_node configure
ros2 lifecycle set /lifecycle_node activate
ros2 lifecycle set /lifecycle_node deactivate
ros2 lifecycle set /lifecycle_node cleanup

⸻

Topic Verification

Verified topic publication:

ros2 topic echo /lifecycle_chatter

Observed:

Lifecycle node running

Publishing occurred only while the node was active.

⸻

Lifecycle Manager Implementation

Created:

lifecycle_manager.py

Implemented:

* ChangeState service client
* Service discovery waiting
* Configure transition request
* Activate transition request

Lifecycle manager automatically performed:

Configure
    ↓
Activate

without using CLI lifecycle commands.

⸻

Lifecycle Manager Verification

Executed:

ros2 run lifecycle_demo lifecycle_manager

Observed:

Lifecycle manager started
Sending configure request
Configure success: True
Sending activate request
Activate success: True

Verified final state:

ros2 lifecycle get /lifecycle_node

Output:

active [3]

⸻

Debugging Performed

Cleanup Crash Investigation

Issue:

Node disappeared after cleanup

Root Cause:

Timer callback attempted to publish after publisher cleanup.

Resolution:

if self.publisher_ is None:
    return

and

self.destroy_timer(self.timer_)

implemented during cleanup.

⸻

Commands Used

ros2 lifecycle nodes
ros2 lifecycle get /lifecycle_node
ros2 lifecycle set /lifecycle_node configure
ros2 lifecycle set /lifecycle_node activate
ros2 lifecycle set /lifecycle_node deactivate
ros2 lifecycle set /lifecycle_node cleanup
ros2 topic echo /lifecycle_chatter
ros2 interface show lifecycle_msgs/srv/ChangeState

⸻

Engineering Outcome

Built a production-style ROS 2 Lifecycle architecture consisting of a Lifecycle Node, Lifecycle Publisher, Lifecycle Manager, managed startup sequence, controlled activation/deactivation, resource cleanup, and automated lifecycle orchestration. Verified behavior through runtime testing, lifecycle CLI tools, service-based management, and state-transition validation.

Status

✅ Module 25 Complete