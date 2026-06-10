# ROS Debug Playbook

## 1. Node Checks

Verify all expected nodes are running:

bash ros2 node list 

Inspect a specific node:

bash ros2 node info <node_name> 

Check:
- Publishers
- Subscribers
- Services
- Parameters

Common Failure:
- Missing node in graph

Recovery:
- Restart launch file
- Verify package build
- Check terminal logs

---

## 2. Topic Checks

List all topics:

bash ros2 topic list 

Inspect topic connections:

bash ros2 topic info <topic_name> 

Check:
- Publisher count
- Subscriber count

Common Failures:
- Publisher count = 0
- Subscriber count = 0
- Missing topic

Recovery:
- Verify source node
- Verify topic names
- Check remappings

---

## 3. Topic Frequency Checks

Measure message rate:

bash ros2 topic hz <topic_name> 

Verify:
- Messages are arriving
- Frequency matches expectations

Common Failures:
- No output
- Unexpected rate
- Intermittent messages

Recovery:
- Verify publisher node
- Inspect timers
- Check system load

---

## 4. Parameter Checks

List parameters:

bash ros2 param list 

Read parameter:

bash ros2 param get <node> <parameter> 

Dump all parameters:

bash ros2 param dump <node> 

Verify:
- Correct YAML profile loaded
- Parameter values match expectations

Common Failures:
- Wrong configuration
- Missing parameters
- Incorrect limits

Recovery:
- Reload YAML file
- Relaunch node
- Update parameter values

---

## 5. Launch Checks

Verify launch file starts all required nodes:

bash ros2 launch <package> <launch_file> 

Check:
- Node names
- Namespace settings
- Parameter files

Common Failures:
- Node not launched
- Incorrect parameter file
- Launch argument errors

Recovery:
- Review launch file
- Verify package paths
- Check launch arguments

---

## 6. Environment Checks

Run:

bash ros2 doctor 

Verify:
- ROS installation health
- DDS communication
- Package availability

Common Failures:
- Unsourced workspace
- Missing dependencies
- DDS issues

Recovery:

bash source /opt/ros/jazzy/setup.bash source install/setup.bash 

Rebuild workspace if needed:

bash colcon build 

---

## 7. Recovery Workflow

When a ROS system appears broken:

1. Run ros2 node list
2. Verify expected nodes exist
3. Run ros2 topic list
4. Verify expected topics exist
5. Run ros2 topic info
6. Check publisher/subscriber counts
7. Run ros2 topic hz
8. Verify messages are flowing
9. Inspect parameters
10. Run ros2 doctor
11. Review launch configuration
12. Restart affected nodes if necessary

This workflow should be followed before modifying source code.