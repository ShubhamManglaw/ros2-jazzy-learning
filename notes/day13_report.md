# Day 13 – ROS 2 Parameters Introduction

Date: 07 June 2026

## Objective

Learn how ROS 2 Parameters allow node behavior to be configured without modifying source code. Understand parameter declaration, retrieval, command-line overrides, and runtime inspection.

---

## Concepts Learned

### 1. ROS 2 Parameters

Parameters provide configurable values for ROS 2 nodes. They replace hardcoded values and allow robot behavior to be adjusted externally.

Example:

Instead of:

python speed = 1.0 

Use:

python self.declare_parameter("max_speed", 1.0) 

This enables runtime configuration.

---

### 2. Declaring Parameters

Parameters must be declared before use.

python self.declare_parameter("robot_name", "NewtonBot") self.declare_parameter("max_speed", 1.0) self.declare_parameter("battery_capacity", 100) 

---

### 3. Reading Parameters

Parameter values can be retrieved using:

python robot_name = self.get_parameter("robot_name").value max_speed = self.get_parameter("max_speed").value battery = self.get_parameter("battery_capacity").value 

---

### 4. Parameter Override from CLI

Parameters can be overridden without modifying code.

bash ros2 run parameter_demo parameter_node \ --ros-args \ -p robot_name:=Go2 \ -p max_speed:=3.5 \ -p battery_capacity:=500 

Output:

text Go2 | Speed=3.5 | Battery=500 

---

### 5. Parameter Inspection Tools

List parameters:

bash ros2 param list 

Get parameter value:

bash ros2 param get /parameter_node robot_name 

Set parameter value:

bash ros2 param set /parameter_node robot_name Atlas 

---

## Implementation

### parameter_node.py

python import rclpy from rclpy.node import Node   class ParameterNode(Node):      def __init__(self):         super().__init__("parameter_node")          self.declare_parameter("robot_name", "NewtonBot")         self.declare_parameter("max_speed", 1.0)         self.declare_parameter("battery_capacity", 100)          robot_name = self.get_parameter("robot_name").value         max_speed = self.get_parameter("max_speed").value         battery = self.get_parameter("battery_capacity").value          self.get_logger().info(             f"{robot_name} | Speed={max_speed} | Battery={battery}"         )   def main(args=None):     rclpy.init(args=args)      node = ParameterNode()      rclpy.spin_once(node)      node.destroy_node()      rclpy.shutdown()   if __name__ == "__main__":     main() 

---

## Build Process

bash colcon build --packages-select parameter_demo source install/setup.bash 

---

## Execution

### Default Run

bash ros2 run parameter_demo parameter_node 

Expected Output:

text NewtonBot | Speed=1.0 | Battery=100 

---

### Override Parameters

bash ros2 run parameter_demo parameter_node \ --ros-args \ -p robot_name:=Go2 \ -p max_speed:=3.5 \ -p battery_capacity:=500 

Output:

text Go2 | Speed=3.5 | Battery=500 

---

## Challenges Faced

### Issue 1: Missing init()

Initially forgot to define the constructor method.

Incorrect:

python class ParameterNode(Node):     super().__init__("parameter_node") 

Fix:

python def __init__(self):     super().__init__("parameter_node") 

---

### Issue 2: Undeclared Parameters

Attempted to access:

python self.get_parameter("max_speed") 

before declaring the parameter.

Solution:

python self.declare_parameter("max_speed", 1.0) 

---

### Issue 3: Class Name Typo

Used different spellings of ParameterNode causing execution errors.

---

## Key Learnings

- Parameters allow configurable node behavior.
- Parameters must be declared before use.
- Parameter values can be overridden at runtime.
- ROS CLI tools can inspect and modify parameters.
- Real robotics systems rely heavily on parameters for tuning and deployment.

---

## Real Robotics Applications

### Navigation

- max_velocity
- goal_tolerance
- inflation_radius

### Cameras

- resolution
- fps
- exposure

### LiDAR

- range
- frequency
- frame_id

### Controllers

- kp
- ki
- kd

---

## Learning Outcomes

After Day 13 I can:

- Create ROS 2 nodes with configurable parameters.
- Declare and retrieve parameter values.
- Override parameters using command-line arguments.
- Inspect parameters using ROS 2 CLI tools.
- Understand how parameters are used in production robotics systems.

---

## Confidence Rating

8/10

Comfortable with basic ROS 2 parameter workflows and ready to move on to YAML-based parameter configuration.

---

## Next Topic

Day 14 – Parameter YAML Files

Learn how to store and load large parameter sets from YAML configuration files, the standard method used in professional ROS 2 robotics projects.