Day 27 Report — Launch System Architecture Engineering

Objective

Learn how ROS 2 launch systems scale from launching individual nodes to orchestrating complete robotic software stacks.

⸻

Architecture Implemented

robot_bringup
└── launch/
    ├── bringup.launch.py
    ├── management.launch.py
    ├── telemetry.launch.py
    └── navigation.launch.py

The main launch file became the system entry point and composed subsystem launch files using launch composition.

⸻

Work Completed

1. Bringup Package Architecture

Used the existing robot_bringup package as the deployment entry point.

Created subsystem launch files:

* management.launch.py
* telemetry.launch.py
* navigation.launch.py

Created a hierarchical startup architecture instead of a flat node-launching design.

⸻

2. Launch Composition

Implemented:

IncludeLaunchDescription(...)

This allowed bringup.launch.py to include and orchestrate subsystem launch files.

Architecture:

bringup.launch.py
        │
        ├── management.launch.py
        ├── telemetry.launch.py
        └── navigation.launch.py

⸻

3. Launch Arguments

Implemented:

DeclareLaunchArgument(
    "simulation",
    default_value="false"
)

Verified using:

ros2 launch robot_bringup bringup.launch.py --show-args

⸻

4. Launch Configuration

Implemented:

simulation = LaunchConfiguration("simulation")

Learned that LaunchConfiguration creates a deferred runtime substitution rather than a normal Python string.

⸻

5. Conditional Launching

Implemented:

condition=IfCondition(simulation)

on the telemetry subsystem.

Behavior:

ros2 launch robot_bringup bringup.launch.py simulation:=true

Loads telemetry subsystem.

ros2 launch robot_bringup bringup.launch.py simulation:=false

Skips telemetry subsystem.

⸻

6. Debugging

Encountered:

UnboundLocalError:
cannot access local variable 'simulation'

Root cause:

simulation was used before being initialized.

Resolution:

Moved:

simulation_arg = DeclareLaunchArgument(...)
simulation = LaunchConfiguration(...)

before any launch actions that referenced them.

⸻

Verification

Commands executed:

colcon build --packages-select robot_bringup
ros2 launch robot_bringup bringup.launch.py
ros2 launch robot_bringup bringup.launch.py --show-args
ros2 launch robot_bringup bringup.launch.py simulation:=true
ros2 launch robot_bringup bringup.launch.py simulation:=false

Results:

* Main launch file executed successfully.
* Nested launch files loaded correctly.
* Launch arguments appeared correctly.
* Conditional launching worked as expected.
* No startup errors after debugging.

⸻

Key Concepts Learned

* Bringup packages
* Launch architecture
* Launch composition
* Nested launch files
* DeclareLaunchArgument
* LaunchConfiguration
* IfCondition
* Runtime deployment configuration
* Launch debugging

⸻

Engineering Takeaway

Launch files are not simply startup scripts. They represent the deployment architecture of a robot system. By organizing subsystems into separate launch files and composing them through a central bringup package, large robotics projects become maintainable, scalable, and configurable across simulation and real hardware environments.

⸻

Module Status

Completed.

All major Module 27 objectives were achieved:

* Main launch file
* Nested launch files
* Launch composition
* Launch arguments
* Launch substitutions
* Conditional startup
* Startup verification
* Launch architecture documentation