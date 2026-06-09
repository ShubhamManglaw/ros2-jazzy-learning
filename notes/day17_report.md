# Day 17 Report – ROS 2 Bringup, Launch Files & Configuration Profiles

Date: 2026-06-09  
Status: Completed ✅  
Duration: ~3.5 Hours

## Objective

Learn how ROS 2 launch files are used to start multiple nodes together, organize robot startup using a bringup package, and load different runtime configurations using YAML parameter files.

---

## Concepts Learned

### 1. Bringup Package

Created a dedicated package:

bash robot_bringup 

Purpose:

- Store launch files
- Store configuration files
- Provide one-command robot startup

---

### 2. Launch Files

Learned how a launch file can start multiple ROS nodes simultaneously.

Nodes launched:

- velocity_source
- velocity_limiter_v3
- velocity_monitor

Single command startup:

bash ros2 launch robot_bringup bringup.launch.py 

---

### 3. LaunchDescription

Learned that a launch file returns a LaunchDescription object containing all actions that should execute during startup.

Example actions:

- Start nodes
- Load parameters
- Declare launch arguments

---

### 4. Package Discovery

Learned how ROS finds installed package resources using:

python get_package_share_directory('robot_bringup') 

This avoids hardcoded filesystem paths.

---

### 5. YAML Configuration Files

Created configuration profiles:

text config/ ├── indoor.yaml ├── outdoor.yaml └── testing.yaml 

Indoor:

yaml max_linear_speed: 0.3 max_angular_speed: 0.5 

Outdoor:

yaml max_linear_speed: 1.0 max_angular_speed: 2.0 

Testing:

yaml max_linear_speed: 0.1 max_angular_speed: 0.2 

---

### 6. Parameter Loading

Loaded YAML parameters into the limiter node using:

python Node(     package='my_first_pkg',     executable='velocity_limiter_v3',     parameters=[config_file] ) 

Verified that YAML values override default values declared inside the node.

---

### 7. Launch Arguments

Implemented runtime profile selection:

bash ros2 launch robot_bringup bringup.launch.py profile:=indoor.yaml  ros2 launch robot_bringup bringup.launch.py profile:=outdoor.yaml  ros2 launch robot_bringup bringup.launch.py profile:=testing.yaml 

Learned how launch arguments allow changing robot behavior without modifying code.

---

## Verification Results

### Indoor Profile

Expected:

text linear = 0.3 angular = 0.5 

Observed:

text Limits: linear=0.3, angular=0.5 Final linear.x=0.3, angular.z=0.5 

---

### Outdoor Profile

Expected:

text linear = 1.0 angular = 2.0 

Observed:

text Limits: linear=1.0, angular=2.0 Final linear.x=1.0, angular.z=1.5 

Angular velocity remained 1.5 because the source node publishes only 1.5.

---

### Testing Profile

Expected:

text linear = 0.1 angular = 0.2 

Observed:

text Limits: linear=0.1, angular=0.2 Final linear.x=0.1, angular.z=0.2 

---

## Package Structure

text robot_bringup/ ├── config │   ├── indoor.yaml │   ├── outdoor.yaml │   └── testing.yaml ├── launch │   └── bringup.launch.py ├── package.xml ├── setup.py └── resource 

---

## Important Learnings

- Executable name and node name are different concepts.
- Launch files should not contain hardcoded paths.
- Configuration should be stored in YAML instead of source code.
- One launch file can support multiple robot profiles.
- ROS launch arguments enable flexible deployments.
- Install space resources must be declared in setup.py.

---

## Debugging & Mistakes

### Mistake 1

Forgot to install launch files through setup.py.

Result:

bash file 'bringup.launch.py' was not found 

Fix:

Added launch directory to data_files.

---

### Mistake 2

Forgot to install YAML configuration files.

Fix:

Added:

python ('share/' + package_name + '/config',  glob('config/*.yaml')) 

to setup.py.

---

### Mistake 3

Accidentally overwrote indoor.yaml while testing.

Fix:

Restored all three configuration profiles.

---

### Mistake 4

Tried to use os.path.join() directly with LaunchConfiguration.

Fix:

Used ROS launch substitutions:

python PathJoinSubstitution FindPackageShare 

---

## Final Outcome

Successfully built a reusable ROS 2 bringup package capable of:

- Launching multiple nodes
- Loading configuration profiles
- Switching runtime behavior through launch arguments
- Managing robot startup from a single command

Day 17 completed successfully.
