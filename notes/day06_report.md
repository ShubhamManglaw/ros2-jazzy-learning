# Day 06 — Control Layer

## Objective

Learn how a ROS2 control layer receives high-level commands and converts them into safe commands before they reach robot hardware.

---

# Big Picture

A robot should not receive commands directly from planners, joysticks, or autonomy systems.

Bad Design:

```text
Joystick
   ↓
Motor Driver
```

Good Design:

```text
Joystick
   ↓
Raw Command
   ↓
Control Layer / Safety Filter
   ↓
Motor Driver
```

The control layer protects the robot from unsafe commands.

---

# Day 6 Pipeline

```text
velocity_source
      ↓
/cmd_vel_raw
      ↓
velocity_limiter
      ↓
/cmd_vel
      ↓
velocity_monitor
```

---

# New ROS Message Type

Unlike Day 5 which used:

```python
Int32
```

Day 6 uses:

```python
geometry_msgs/msg/Twist
```

Inspect message:

```bash
ros2 interface show geometry_msgs/msg/Twist
```

Structure:

```text
Twist
├── linear
│   ├── x
│   ├── y
│   └── z
└── angular
    ├── x
    ├── y
    └── z
```

Most important fields for ground robots:

```text
linear.x
angular.z
```

Meaning:

```text
linear.x  → forward/backward velocity
angular.z → turning velocity
```

---

# Node 1 — Velocity Source

Purpose:

Generate raw velocity commands.

Publishes:

```text
/cmd_vel_raw
```

Message Type:

```python
Twist
```

Published Values:

```python
msg.linear.x = 2.0
msg.angular.z = 1.5
```

Output Example:

```text
linear.x=2.0
angular.z=1.5
```

---

# Node 2 — Velocity Limiter

Purpose:

Apply safety limits before commands reach the robot.

Subscribes:

```text
/cmd_vel_raw
```

Publishes:

```text
/cmd_vel
```

Safety Limits:

```text
linear.x  ∈ [-0.5, 0.5]
angular.z ∈ [-1.0, 1.0]
```

Limiting Logic:

```python
final.linear.x = max(-0.5, min(msg.linear.x, 0.5))
final.angular.z = max(-1.0, min(msg.angular.z, 1.0))
```

Examples:

```text
2.0  → 0.5
0.3  → 0.3
-2.0 → -0.5
```

```text
1.5  → 1.0
0.8  → 0.8
-3.0 → -1.0
```

---

# Node 3 — Velocity Monitor

Purpose:

Monitor and display safe commands.

Subscribes:

```text
/cmd_vel
```

Output Example:

```text
Received:
linear.x=0.5
angular.z=1.0
```

No publisher required.

No timer required.

---

# Verification

Run all nodes:

Terminal 1:

```bash
ros2 run my_first_pkg velocity_source
```

Terminal 2:

```bash
ros2 run my_first_pkg velocity_limiter
```

Terminal 3:

```bash
ros2 run my_first_pkg velocity_monitor
```

Observed Output:

```text
Received: linear.x=0.5, angular.z=1.0
```

This confirms that unsafe commands were successfully filtered.

---

# Useful Commands

List nodes:

```bash
ros2 node list
```

List topics:

```bash
ros2 topic list
```

Inspect raw commands:

```bash
ros2 topic echo /cmd_vel_raw
```

Inspect filtered commands:

```bash
ros2 topic echo /cmd_vel
```

Check topic connections:

```bash
ros2 topic info /cmd_vel_raw
ros2 topic info /cmd_vel
```

View ROS graph:

```bash
rqt_graph
```

---

# Key Learnings

### Control Layer

A control layer sits between command generation and hardware execution.

### Raw vs Safe Commands

```text
Raw Command
      ↓
Safety Filter
      ↓
Safe Command
```

### Processing Nodes

A processing node acts as:

```text
Subscriber
      ↓
Process Data
      ↓
Publisher
```

### Why Filters Matter

Without a limiter:

```text
2.0 m/s
1.5 rad/s
```

reaches the robot.

With a limiter:

```text
0.5 m/s
1.0 rad/s
```

becomes the maximum allowed command.

---

# Common Mistakes

### Wrong Import

Incorrect:

```python
from std_msgs.msg import Twist
```

Correct:

```python
from geometry_msgs.msg import Twist
```

### Publishing Raw and Safe Commands on Same Topic

Bad:

```text
/cmd_vel
```

for both input and output.

Correct:

```text
/cmd_vel_raw
/cmd_vel
```

### Forgetting Negative Limits

Bad:

```python
value if value < max_limit else max_limit
```

Correct:

```python
max(-limit, min(value, limit))
```

### Multiple Publishers on /cmd_vel

Always verify:

```bash
ros2 topic info /cmd_vel
```

---

# Real Robotics Connection

This architecture appears in:

```text
Teleoperation
Navigation
Autonomous Robots
Warehouse AMRs
Delivery Robots
Unitree Robots
Nav2
```

Pattern:

```text
Planner
   ↓
Control Layer
   ↓
Motor Driver
```

---

# Day 6 Outcome

Successfully built a ROS2 control pipeline using Twist messages.

Implemented:

* velocity_source
* velocity_limiter
* velocity_monitor

Verified safe command generation and control-layer behavior.

Readiness for Day 7: HIGH
