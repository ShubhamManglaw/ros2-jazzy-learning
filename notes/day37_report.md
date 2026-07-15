# Day 36 Report — Module 37: DDS & Middleware Engineering

**Date:** July 16, 2026  
**Roadmap Phase:** Phase 4 — Advanced Robotics Engineering  
**Module:** 37 — DDS & Middleware Engineering  
**Workspace:** `~/ros2-jazzy-learning`  
**Status:** ✅ Completed

---

# Objective

Understand the internal communication architecture of ROS 2, including DDS, middleware abstraction, Quality of Service (QoS), automatic discovery, performance engineering, debugging techniques, and practical communication analysis.

---

# Topics Covered

## 1. Why ROS 2 Uses DDS

Learned why ROS 2 replaced the ROS Master architecture used in ROS 1.

Key points:

- DDS provides decentralized communication.
- Nodes automatically discover each other.
- No central master exists.
- Communication scales better for distributed robotic systems.
- Middleware handles networking so application code remains simple.

---

## 2. ROS 2 Communication Stack

Studied the complete communication pipeline:

```
Application
      ↓
rclcpp / rclpy
      ↓
RMW Interface
      ↓
DDS Implementation
      ↓
Operating System
      ↓
Network
      ↓
DDS
      ↓
Subscriber
```

Key understanding:

- ROS nodes never communicate directly.
- DDS is responsible for discovery, transport, reliability, and QoS.

---

## 3. DDS Architecture

Learned the major DDS entities.

### Domain Participant

Represents one application inside a DDS domain.

### Topic

Defines:

- Topic name
- Message type

A Topic is not the data itself.

### DataWriter

Responsible for publishing data into DDS.

### DataReader

Receives DDS data and delivers it to ROS subscribers.

---

## 4. Automatic Discovery

Studied how DDS automatically discovers publishers and subscribers.

Discovery compares:

- Topic name
- Message type
- QoS compatibility
- DDS Domain ID

No IP addresses or ports are manually configured.

---

## 5. Quality of Service (QoS)

Studied all major QoS policies.

### Reliability

- Reliable
- Best Effort

### Durability

- Volatile
- Transient Local

### History

- Keep Last
- Keep All

### Deadline

Expected update frequency.

### Lifespan

Maximum valid lifetime of a message.

### Liveliness

Detects whether publishers are still alive.

---

## 6. DDS Vendors

Studied the role of multiple DDS implementations.

Covered:

- Fast DDS
- Cyclone DDS
- Connext DDS
- GurumDDS

Learned how the RMW layer allows switching middleware without changing application code.

---

## 7. Performance Engineering

Studied communication performance metrics.

### Latency

Time required for one message to travel.

### Throughput

Amount of data transferred per second.

### Bandwidth

Maximum network capacity.

Also discussed:

- Network congestion
- Large messages
- Subscriber bottlenecks
- QoS impact on performance

---

## 8. DDS Debugging Workflow

Learned a systematic debugging approach.

Checklist:

1. Verify nodes are running.
2. Verify topic names.
3. Verify message types.
4. Verify ROS_DOMAIN_ID.
5. Verify QoS compatibility.
6. Verify DDS discovery.
7. Verify network connectivity.

Important ROS 2 tools:

- `ros2 node list`
- `ros2 topic list`
- `ros2 topic info`
- `ros2 topic info --verbose`
- `ros2 topic hz`
- `ros2 topic bw`
- `ros2 topic echo`

---

# Practical Exercises Performed

## 1. Node Discovery

Command:

```bash
ros2 node list
```

Observed:

```
/listener
/talker
```

Confirmed automatic DDS discovery.

---

## 2. QoS Inspection

Command:

```bash
ros2 topic info /chatter --verbose
```

Observed:

Publisher:

- Reliability: RELIABLE
- Durability: VOLATILE
- Lifespan: Infinite
- Deadline: Infinite
- Liveliness: AUTOMATIC

Subscriber:

- Reliability: RELIABLE
- Durability: VOLATILE
- Lifespan: Infinite
- Deadline: Infinite
- Liveliness: AUTOMATIC

Also confirmed:

- Publisher count: 1
- Subscriber count: 1
- Message type:
  `std_msgs/msg/String`

---

## 3. Publishing Frequency

Command:

```bash
ros2 topic hz /chatter
```

Observed:

Average frequency:

```
1.000 Hz
```

Meaning:

The demo talker publishes one message every second.

---

## 4. Bandwidth Measurement

Command:

```bash
ros2 topic bw /chatter
```

Observed:

Approximate bandwidth:

```
30–41 B/s
```

Average message size:

```
28 Bytes
```

Observation:

Small text messages consume negligible bandwidth compared to camera or LiDAR topics.

---

## 5. Live Topic Inspection

Command:

```bash
ros2 topic echo /chatter
```

Observed:

```
Hello World: 129
Hello World: 130
Hello World: 131
```

Confirmed successful end-to-end communication.

---

# Engineering Insights Gained

- ROS 2 communication is completely middleware-driven.
- DDS performs automatic node discovery without a master server.
- Publishers and subscribers communicate through DataWriters and DataReaders.
- QoS policies directly influence communication behavior.
- DDS vendors can be swapped transparently through the RMW layer.
- Communication issues are often configuration problems rather than coding bugs.
- Performance engineering requires balancing latency, throughput, and bandwidth according to application requirements.

---

# Commands Practiced

```bash
ros2 node list

ros2 topic list

ros2 topic info /chatter

ros2 topic info /chatter --verbose

ros2 topic hz /chatter

ros2 topic bw /chatter

ros2 topic echo /chatter
```

---

# Deliverables Completed

- ✅ DDS architecture understanding
- ✅ Middleware architecture understanding
- ✅ Automatic discovery concepts
- ✅ QoS concepts
- ✅ DDS vendor comparison
- ✅ Communication performance concepts
- ✅ DDS debugging workflow
- ✅ Practical DDS inspection using ROS 2 CLI
- ✅ Communication analysis experiments

---

# Module Completion Summary

| Lesson | Status |
|---------|--------|
| Why DDS Exists | ✅ |
| DDS Architecture | ✅ |
| Automatic Discovery | ✅ |
| Quality of Service | ✅ |
| DDS Vendors | ✅ |
| Performance Engineering | ✅ |
| DDS Debugging | ✅ |
| Hands-on Communication Analysis | ✅ |

**Module Completion:** **100%**

---

# Key Takeaways

This module provided a deep understanding of the communication infrastructure that powers ROS 2. Rather than viewing topics as direct connections between nodes, I now understand the layered architecture involving the RMW interface, DDS middleware, DataWriters, DataReaders, and QoS policies. I also gained practical experience inspecting live communication using ROS 2 CLI tools, measuring publish rates and bandwidth, and analyzing QoS configurations. This knowledge forms the communication foundation required for advanced topics such as distributed robotics, multi-computer systems, MoveIt 2, Navigation2, and future capstone projects including the 6-DOF robotic arm and AUV.

---

# Next Module

**Module 38 — Distributed Robotics Networking Engineering**