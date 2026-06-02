# ROS 2 Node Notes

## What is a Node?

A node is the smallest executable unit in ROS 2.

A ROS system is built from multiple nodes that communicate with each other using topics, services, actions, and parameters.

Example:

```text
DistancePublisher Node
        ↓
ultrasonic_distance Topic
        ↓
DistanceSubscriber Node
```

Both the publisher and subscriber are separate ROS 2 nodes.

---

## Why Do We Use Nodes?

Nodes allow us to separate robot functionality into independent modules.

Example:

```text
Camera Node
Lidar Node
Navigation Node
Motor Controller Node
Battery Monitor Node
```

Each node performs one responsibility.

Benefits:

* Modular
* Easy to debug
* Reusable
* Distributed across multiple computers

---

## Creating a Node

Every custom Python node inherits from:

```python
Node
```

Example:

```python
class DistancePublisher(Node):
```

or

```python
class DistanceSubscriber(Node):
```

Inheritance gives access to ROS 2 features.

---

## Node Initialization

Inside every node:

```python
super().__init__('node_name')
```

Example:

```python
super().__init__('distance_publisher')
```

or

```python
super().__init__('distance_subscriber')
```

This:

* Creates the ROS node
* Registers the node with ROS
* Assigns the node name

---

## What Does a Node Gain?

By inheriting from Node, a class can create:

### Publishers

```python
self.create_publisher(...)
```

Used to send messages.

---

### Subscribers

```python
self.create_subscription(...)
```

Used to receive messages.

---

### Timers

```python
self.create_timer(...)
```

Used to execute code periodically.

---

### Logger

```python
self.get_logger().info(...)
```

Used for ROS logging.

---

### Parameters

```python
self.declare_parameter(...)
```

Used to configure node behavior.

---

## Node Lifecycle

```text
rclpy.init()
      ↓
Node Creation
      ↓
Publishers/Subscribers Created
      ↓
rclpy.spin(node)
      ↓
Callbacks Execute
      ↓
destroy_node()
      ↓
rclpy.shutdown()
```

---

## Example Publisher Node

```python
class DistancePublisher(Node):

    def __init__(self):
        super().__init__('distance_publisher')
```

Responsibilities:

* Create publisher
* Create timer
* Generate messages
* Publish messages

---

## Example Subscriber Node

```python
class DistanceSubscriber(Node):

    def __init__(self):
        super().__init__('distance_subscriber')
```

Responsibilities:

* Create subscription
* Receive messages
* Process messages
* Make decisions

---

## Event Driven Architecture

Publisher:

```text
Timer
 ↓
Callback Runs
 ↓
Publish Message
```

Subscriber:

```text
Message Arrives
 ↓
Callback Runs
 ↓
Process Message
```

Subscribers do not require timers.

Incoming messages automatically trigger callbacks.

---

## Important Commands

List nodes:

```bash
ros2 node list
```

Node information:

```bash
ros2 node info /distance_publisher
```

Node information:

```bash
ros2 node info /distance_subscriber
```

---

## Day 1–4 Examples

Node Names:

```text
distance_publisher
distance_subscriber
```

Topics:

```text
ultrasonic_distance
```

Publisher Callback:

```python
publish_distance()
```

Subscriber Callback:

```python
listener_callback(msg)
```

---

## Interview Definition

A ROS 2 node is an independent executable process that performs a specific task and communicates with other nodes using ROS communication mechanisms such as topics, services, actions, and parameters.

---

## Key Takeaways

* Node = smallest executable unit in ROS 2
* Every custom ROS program is a node
* Nodes inherit from `Node`
* Nodes communicate through topics
* Publishers send messages
* Subscribers receive messages
* Timers trigger periodic callbacks
* `rclpy.spin()` keeps nodes alive
* Multiple nodes form a complete robot system
