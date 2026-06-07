# Day 14 Report — Runtime Parameter Tuning

## Overview

Day 14 focused on upgrading the Day 6 velocity limiter into a runtime-configurable safety controller. The objective was to replace hardcoded velocity limits with ROS 2 parameters and verify that robot behavior could be modified without rebuilding or restarting the node.

---

## Objectives

- Convert hardcoded velocity limits into ROS 2 parameters
- Tune robot behavior while the system is running
- Learn ROS 2 parameter inspection tools
- Verify parameter changes affect system behavior
- Compare raw and filtered velocity commands

---

## System Architecture

text velocity_source       ↓ /cmd_vel_raw       ↓ velocity_limiter_v2       ↓ /cmd_vel       ↓ velocity_monitor 

---

## Implementation

### Original Limiter

The original implementation used fixed values:

python final.linear.x = max(-0.5, min(msg.linear.x, 0.5)) final.angular.z = max(-1.0, min(msg.angular.z, 1.0)) 

### Upgraded Limiter

The limiter was modified to use ROS 2 parameters:

python self.declare_parameter("max_linear_speed", 0.5) self.declare_parameter("max_angular_speed", 1.0) 

Runtime values are read inside the callback:

python max_linear = self.get_parameter(     "max_linear_speed" ).value  max_angular = self.get_parameter(     "max_angular_speed" ).value 

Velocity commands are clamped using the parameter values:

python final.linear.x = max(     -max_linear,     min(msg.linear.x, max_linear) )  final.angular.z = max(     -max_angular,     min(msg.angular.z, max_angular) ) 

---

## Parameter Inspection

### Parameter Description

bash ros2 param describe /velocity_limiter max_linear_speed 

Output:

text Parameter name: max_linear_speed Type: double 

### Parameter Dump

bash ros2 param dump /velocity_limiter 

Output:

yaml /velocity_limiter:   ros__parameters:     max_angular_speed: 1.0     max_linear_speed: 0.5 

---

## Runtime Tuning

### Initial Value

bash ros2 param get /velocity_limiter max_linear_speed 

Result:

text 0.5 

### Parameter Update

bash ros2 param set /velocity_limiter max_linear_speed 0.2 

Result:

text Set parameter successful 

No node restart or rebuild was required.

---

## Behavior Verification

### Raw Velocity Input

bash ros2 topic echo /cmd_vel_raw 

Output:

text linear.x = 2.0 angular.z = 1.5 

### Limited Velocity Output

bash ros2 topic echo /cmd_vel 

Output:

text linear.x = 0.5 angular.z = 1.0 

### After Runtime Tuning

After setting:

bash ros2 param set /velocity_limiter max_linear_speed 0.2 

Velocity monitor output became:

text linear.x = 0.2 angular.z = 1.0 

This confirmed that the limiter immediately adopted the new parameter value while running.

---

## Commands Used

bash ros2 param list ros2 param get /velocity_limiter max_linear_speed ros2 param set /velocity_limiter max_linear_speed 0.2 ros2 param describe /velocity_limiter max_linear_speed ros2 param dump /velocity_limiter ros2 topic echo /cmd_vel_raw ros2 topic echo /cmd_vel 

---

## Challenges and Debugging

### Issue

Initially it was unclear whether changing a parameter would automatically affect node behavior.

### Resolution

The parameter values were moved inside the callback using:

python self.get_parameter(...).value 

This ensured every incoming message used the latest parameter values, enabling true runtime tuning.

---

## Key Learnings

- Parameters store configuration but do not automatically affect behavior.
- Node logic must actively read parameter values.
- Runtime tuning allows safer and faster experimentation.
- Configuration should be separated from source code.
- ROS 2 provides powerful tools for parameter inspection and modification.

---

## Engineering Reflection

### Why didn't ROS automatically change behavior when the parameter changed?

Because parameters only store values. The node must explicitly read and use those values inside its logic.

### Why should parameters be read inside callbacks?

Reading parameters inside callbacks ensures the latest parameter values are applied to every incoming message.

### What robotics systems commonly require runtime tuning?

- Navigation controllers
- PID controllers
- Motor speed limiters
- Sensor filters
- SLAM systems
- Obstacle avoidance systems

### What risks exist if limits are hardcoded?

- Difficult deployment across different robots
- Requires source code modification
- Increases maintenance effort
- Makes field tuning difficult
- Can create safety risks

---

## Deliverables Completed

- ✅ velocity_limiter_v2 implemented
- ✅ Runtime parameter tuning verified
- ✅ Parameter inspection completed
- ✅ Raw vs filtered command comparison completed
- ✅ Parameter dump completed
- ✅ Engineering reflection completed

---

## Final Outcome

Day 14 successfully transformed a fixed velocity limiter into a configurable robotics safety component. The node now supports live parameter tuning, enabling robot behavior to be adjusted without code changes, rebuilds, or restarts. This lays the foundation for Day 15, where these parameters will be moved into YAML configuration profiles for deployment.