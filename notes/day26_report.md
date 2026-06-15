Day 26 Report — Component Architecture & Composable Nodes Engineering

Completion Date

2026-06-15

⸻

Objective

Learn how ROS 2 Components and Composable Nodes work by building a dynamically loadable component, registering it with pluginlib, loading it into a Component Container, verifying runtime execution, and unloading it without restarting the process.

This module introduced a major architectural shift from standalone ROS nodes toward reusable shared-library-based software components.

⸻

Why This Module Matters

In previous modules every ROS node was launched as a separate process:

Node A → Process A
Node B → Process B
Node C → Process C

This architecture is simple but introduces:

* Memory overhead
* Process scheduling overhead
* Context switching
* IPC communication overhead

ROS 2 Components solve this by allowing multiple nodes to run inside a single process:

Component Container
├── Camera Component
├── Localization Component
├── Navigation Component
└── Diagnostics Component

This architecture is heavily used in Navigation2, MoveIt2 and production robotics systems.

⸻

New C++ Concepts Learned

Header and Source Separation

For the first time a class was split into:

camera_component.hpp
camera_component.cpp

Header file:

class CameraComponent
{
};

Purpose:

* Declare interfaces
* Declare class members
* Declare methods

Source file:

CameraComponent::CameraComponent(...)
{
}

Purpose:

* Implement functionality

⸻

Scope Resolution Operator

Learned:

CameraComponent::CameraComponent(...)

Meaning:

Constructor belonging to CameraComponent

The scope resolution operator:

::

is used to define functions outside the class declaration.

⸻

Constructor Initializer List

Learned:

: Node(
    "camera_component",
    options
)

Equivalent ROS Python concept:

super().__init__(
    "camera_component"
)

Purpose:

* Initialize the base class
* Pass NodeOptions from the component container

⸻

Member Variables

Created:

publisher_
timer_

Stored as:

rclcpp::Publisher<std_msgs::msg::String>::SharedPtr
rclcpp::TimerBase::SharedPtr

These are class-owned ROS resources.

⸻

this Pointer

Learned:

this->create_publisher(...)

Equivalent Python concept:

self.create_publisher(...)

Meaning:

Use the current object instance

⸻

std::bind

Learned:

std::bind(
    &CameraComponent::timer_callback,
    this
)

Purpose:

Bind a class method to a timer callback

Equivalent Python concept:

self.timer_callback

⸻

C++ Strings

Learned:

msg.data.c_str()

Purpose:

Convert:

std::string

to:

const char *

for logging macros.

⸻

Component Implementation

Created:

my_robot_components

Package type:

ament_cmake

⸻

CameraComponent

Implemented:

class CameraComponent :
    public rclcpp::Node

Features:

* Publisher
* Timer
* Logging
* Component registration

⸻

Publisher

Created:

camera_data

Topic type:

std_msgs/msg/String

⸻

Timer

Created:

create_wall_timer(
    std::chrono::seconds(1)
)

Behavior:

Every second
    ↓
Publish message

⸻

Callback

Implemented:

void timer_callback()

Behavior:

Create message
    ↓
Populate data
    ↓
Publish
    ↓
Log output

⸻

Pluginlib Registration

Added:

RCLCPP_COMPONENTS_REGISTER_NODE(
    my_robot_components::CameraComponent
)

Purpose:

Make component discoverable

Without registration:

ros2 component types

cannot find the component.

⸻

CMake Configuration

Implemented:

add_library(
  camera_component
  SHARED
  src/camera_component.cpp
)

Generated:

libcamera_component.so

⸻

Added:

ament_target_dependencies(...)

for:

* rclcpp
* rclcpp_components
* pluginlib
* std_msgs

⸻

Added:

rclcpp_components_register_nodes(...)

for runtime discovery.

⸻

Added:

install(...)

for workspace installation.

⸻

Build Verification

Executed:

colcon build --packages-select my_robot_components

Result:

Build successful

Verified:

* Header compilation
* Source compilation
* Shared library generation
* Component registration

⸻

Component Discovery Verification

Executed:

ros2 component types

Observed:

my_robot_components
  my_robot_components::CameraComponent

Verified:

Component discovered successfully

⸻

Container Verification

Started container:

ros2 run rclcpp_components component_container

Container launched successfully.

⸻

Dynamic Loading Verification

Executed:

ros2 component load \
/ComponentManager \
my_robot_components \
my_robot_components::CameraComponent

Observed:

Loaded component 1

Verified:

Runtime loading successful

⸻

Runtime Verification

Executed:

ros2 node list

Observed:

/ComponentManager
/camera_component

Verified:

Component instantiated successfully

⸻

Executed:

ros2 topic list

Observed:

/ camera_data

Verified:

Publisher created successfully

⸻

Executed:

ros2 topic echo /camera_data

Observed:

Camera component publishing

Verified:

Data flow operational

⸻

Dynamic Unload Verification

After component removal:

/camera_component disappeared
/camera_data disappeared

Verified:

Component lifecycle managed by container

without restarting the process.

⸻

Engineering Outcome

Built a complete ROS 2 Component Architecture using:

* Shared libraries
* Component containers
* Pluginlib registration
* Dynamic loading
* Dynamic unloading
* Publisher and timer execution

Successfully transitioned from standalone ROS nodes to reusable composable node architecture used in large-scale robotics systems.

⸻

Key Takeaways

1. Components are ROS nodes compiled as shared libraries.
2. Components run inside containers.
3. Pluginlib enables runtime discovery and loading.
4. Containers reduce process overhead.
5. Dynamic loading avoids restarting systems.
6. Dynamic unloading enables runtime reconfiguration.
7. Navigation2 heavily relies on component architecture.
8. C++ class structure is essential for component development.
9. Header/source separation is standard ROS2 C++ design.
10. Component architecture is a foundational building block for scalable robotics software.

Status

✅ Module 26 Complete
✅ Component Discovery Verified
✅ Dynamic Loading Verified
✅ Runtime Communication Verified
✅ Dynamic Unloading Verified
✅ First ROS2 C++ Component Successfully Implemented