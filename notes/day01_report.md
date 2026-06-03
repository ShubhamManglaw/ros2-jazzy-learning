# Day 1 - ROS2 Foundations

Date: 2026-05-29

## Objectives Completed

- Installed ROS2 Jazzy on Ubuntu 24.04
- Created ROS2 workspace
- Understood workspace architecture
- Learned colcon build workflow
- Learned overlay concept
- Created first ROS2 package
- Built first publisher node
- Built first subscriber node
- Verified topic communication

---

## Concepts Learned

### Workspace

A workspace is a collection of ROS packages managed together.

Structure:

```text
src/
build/
install/
log/
```

### Colcon

Colcon discovers packages, resolves dependencies, and builds them in the correct order.

### Overlay

After building, sourcing:

```bash
source install/setup.bash
```

adds the workspace into the ROS environment.

### Publisher

Publishes messages onto a topic.

### Subscriber

Receives messages from a topic through callbacks.

### Callback

A function automatically executed when an event occurs.

### Spin

```python
rclpy.spin(node)
```

keeps the node alive and processes callbacks.

---

## Debugging Log

### Error 1

AttributeError:

module 'my_first_pkg.publisher_node' has no attribute 'main'

Cause:
- publisher_node.py was not saved.

Fix:
- Saved file and rebuilt workspace.

### Error 2

Package not found

Cause:
- Workspace build/source state mismatch.

Fix:
- Rebuilt workspace and sourced install/setup.bash.

---

## Independent Build Score

Level: 2/5

Meaning:
- Modified and understood tutorial code.
- Not yet able to implement from memory.

---

## Failure Severity

Medium

Failures encountered:
- Unsaved source file
- Package discovery confusion

Learning gained:
- Better understanding of ROS build and install process.

---

## Revision Questions

1. Why is source install/setup.bash required?
2. What does rclpy.spin() do?
3. Why does a subscriber not need a timer?
4. What is a callback?
5. Why did the subscriber start at message #256 instead of #0?
