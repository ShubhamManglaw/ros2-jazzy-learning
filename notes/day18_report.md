# Day 18 Report — Multi-Robot Profiles

Date: June 9, 2026  
Package: robot_bringup  
Status: Completed ✅

---

# Objective

Build a scalable multi-robot deployment system where multiple robot types can be launched from the same ROS 2 codebase using different YAML configuration profiles.

---

# Tasks Completed

## 1. Created Robot Profiles

Created three robot-specific configuration files inside:

text robot_bringup/config/ 

### go2.yaml

yaml /velocity_limiter:   ros__parameters:     max_linear_speed: 1.5     max_angular_speed: 3.0 

### warehouse_bot.yaml

yaml /velocity_limiter:   ros__parameters:     max_linear_speed: 0.4     max_angular_speed: 0.8 

### delivery_bot.yaml

yaml /velocity_limiter:   ros__parameters:     max_linear_speed: 0.8     max_angular_speed: 1.5 

---

## 2. Updated Bringup Launch File

Added launch argument support:

python DeclareLaunchArgument(     'robot',     default_value='go2.yaml' ) 

Configuration selection:

python config_file = PathJoinSubstitution([     FindPackageShare('robot_bringup'),     'config',     LaunchConfiguration('robot') ]) 

Loaded into:

python Node(     package='my_first_pkg',     executable='velocity_limiter_v3',     parameters=[config_file] ) 

---

## 3. Runtime Verification

### GO2

Command:

bash ros2 launch robot_bringup bringup.launch.py 

Output:

text Limits: linear=1.5, angular=3.0 Final linear.x=1.5, angular.z=1.5 

---

### Delivery Bot

Command:

bash ros2 launch robot_bringup bringup.launch.py robot:=delivery_bot.yaml 

Output:

text Limits: linear=0.8, angular=1.5 Final linear.x=0.8, angular.z=1.5 

---

### Warehouse Bot

Command:

bash ros2 launch robot_bringup bringup.launch.py robot:=warehouse_bot.yaml 

Output:

text Limits: linear=0.4, angular=0.8 Final linear.x=0.4, angular.z=0.8 

---

# Comparison Table

| Robot | Max Linear Speed | Max Angular Speed | Intended Use |
|---------|---------|---------|---------|
| GO2 | 1.5 | 3.0 | Fast mobile robot / quadruped |
| Delivery Bot | 0.8 | 1.5 | Indoor delivery applications |
| Warehouse Bot | 0.4 | 0.8 | Safe warehouse navigation |

---

# Improvements Added

## Reduced Console Spam

Added log throttling using:

python self.log_counter += 1  if self.log_counter % 5 == 0: 

Result:

- Cleaner terminal output
- Easier profile comparison
- Less debugging noise

---

# Issues Encountered

## Launch File Not Updating

Problem:

Launch file changes appeared ignored.

Cause:

Workspace had not been rebuilt and sourced after modifications.

Fix:

bash colcon build source install/setup.bash 

Verification:

bash grep -n "default_value" \ ~/ros2-jazzy-learning/src/robot_bringup/launch/bringup.launch.py 

Confirmed:

python default_value='go2.yaml' 

---

# Engineering Reflection

### Why is maintaining separate codebases for each robot a bad idea?

Maintaining multiple codebases increases maintenance cost, duplicates bugs, and slows development. A single codebase is easier to test and update.

### How do robot manufacturers reuse software across products?

They reuse the same software stack and modify robot behavior using configuration files and launch parameters.

### What parameters differ between robots?

Examples:

- Maximum speed
- Acceleration limits
- Payload limits
- Wheel radius
- Sensor configuration
- Navigation settings

### Why should deployment differences be configuration-driven?

Configuration changes do not require source code modifications or rebuilding, making deployment faster, safer, and easier to maintain.

---

# Final Repository Structure

text robot_bringup/ ├── launch/ │   └── bringup.launch.py ├── config/ │   ├── go2.yaml │   ├── warehouse_bot.yaml │   ├── delivery_bot.yaml │   ├── indoor.yaml │   ├── outdoor.yaml │   └── testing.yaml └── README.md 

---

# Outcome

Successfully implemented a multi-robot deployment architecture where:

- One codebase supports multiple robot types
- Launch arguments select robot behavior
- YAML profiles control runtime configuration
- No source code changes are required when switching robots

This is the first step toward a production-scale robot fleet architecture.