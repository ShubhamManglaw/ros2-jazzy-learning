Day 38 Report — Distributed Robotics Networking Engineering

Date: July 16, 2026

Module: 38 — Distributed Robotics Networking Engineering

Status: ✅ Completed

⸻

Objective

The objective of this module was to understand how ROS 2 enables multiple computers to communicate seamlessly in distributed robotic systems. Unlike previous modules, the emphasis was on system architecture, deployment, networking concepts, and debugging rather than writing ROS 2 code.

⸻

Topics Covered

1. Why Distributed Robotics Exists

Learned why modern robots are rarely built around a single computer.

Studied how professional robots distribute workloads across multiple computers to improve:

* Scalability
* Reliability
* Fault isolation
* Real-time performance
* Maintainability

Real-world examples discussed:

* Industrial robotic manipulators
* Autonomous Underwater Vehicles (AUVs)
* Warehouse robots
* Humanoid robots

⸻

2. ROS 1 vs ROS 2 Networking

Understood the architectural difference between ROS 1 and ROS 2.

ROS 1

* Central ROS Master
* Single point of failure
* Every node must register with the Master

ROS 2

* No ROS Master
* Peer-to-peer architecture
* Automatic discovery using DDS
* Better scalability for distributed robotic systems

⸻

3. DDS Discovery

Studied how ROS 2 nodes discover each other.

Learned that every ROS 2 process creates a DDS Participant which:

* Announces its existence
* Advertises topics
* Advertises services
* Advertises actions
* Exchanges QoS information

Communication flow:

ROS Node
    ↓
DDS Participant
    ↓
Network Discovery
    ↓
Publisher ↔ Subscriber

Important takeaway:

DDS exchanges metadata first, then establishes direct communication.

⸻

4. ROS_DOMAIN_ID

Learned the purpose of DDS Domains.

A DDS Domain isolates robots sharing the same physical network.

Example:

Robot Arm
ROS_DOMAIN_ID = 10
AUV
ROS_DOMAIN_ID = 20

Robots with different domain IDs never discover each other.

Key takeaway:

ROS_DOMAIN_ID affects discovery, not application code.

⸻

5. Networking Fundamentals for Robotics

Focused only on networking concepts required by robotics engineers.

Covered:

IP Address

Unique address of every computer on a network.

Example:

Ubuntu
192.168.1.10
MacBook
192.168.1.15

⸻

LAN

Local Area Network where multiple computers communicate directly.

Examples:

* Home Wi-Fi
* Robotics laboratory
* Industrial Ethernet network

⸻

Ethernet vs Wi-Fi

Ethernet

Advantages:

* Low latency
* Reliable
* Stable communication
* Preferred for robot control

Wi-Fi

Advantages:

* Convenient
* Flexible

Disadvantages:

* Packet loss
* Interference
* Variable latency

⸻

Latency

Time required for data to travel between computers.

Lower latency is essential for:

* Robot control
* Motion planning
* Sensor synchronization

⸻

Bandwidth

Amount of data transferable per second.

Large consumers include:

* Cameras
* LiDAR
* Point clouds
* Video streams

⸻

Packet Loss

Loss of network packets during transmission.

Impacts:

* Vision systems
* Sensor streams
* Teleoperation

Critical control messages require reliable delivery.

⸻

6. Multicast vs Unicast

Learned how DDS performs discovery.

Multicast

Used primarily during discovery.

Participant
↓
Multicast Discovery
↓
Other Participants

Advantages:

* Automatic discovery
* Simple configuration

Potential issues:

* Enterprise networks
* VPNs
* Some Wi-Fi routers
* Firewalls

⸻

Unicast

After successful discovery, data communication typically becomes direct between publisher and subscriber.

Example:

Robot
↓
RViz

This minimizes unnecessary network traffic.

⸻

7. Multi-Machine ROS 2 Deployment

Studied deployment requirements for multiple computers.

Requirements:

* Same network
* Same ROS_DOMAIN_ID
* Compatible DDS implementation
* Correct workspace sourced
* Firewall allows communication

Deployment workflow:

Network
↓
ROS Environment
↓
DDS Discovery
↓
Application Communication

⸻

8. QoS in Distributed Systems

Learned that successful discovery does not guarantee successful communication.

Possible causes of failure:

* QoS mismatch
* Topic type mismatch
* Middleware incompatibility

Important distinction:

Discovery and message exchange are separate stages.

⸻

9. Professional Debugging Workflow

Learned a systematic debugging methodology.

Order of debugging:

1. Network connectivity (ping)
2. ROS_DOMAIN_ID
3. DDS implementation
4. Node discovery
5. Topic discovery
6. QoS inspection
7. Application logic

This prevents wasting time debugging application code when the problem exists at a lower layer.

⸻

10. Production Robotics Architecture

Studied how professional robots are organized.

Typical architecture:

Operator Laptop
│
├── RViz
├── Monitoring
└── Teleoperation
↓
Robot Computer
│
├── Controllers
├── MoveIt
├── Drivers
└── Sensors
↓
GPU Computer
│
├── AI
├── Vision
└── Planning

Key design principles:

* Separate AI from real-time control
* Prefer Ethernet for deterministic communication
* Assign one responsibility per computer
* Scale horizontally by adding computers
* Debug systems layer by layer

⸻

Commands Learned

echo $ROS_DOMAIN_ID
echo $RMW_IMPLEMENTATION
ros2 node list
ros2 topic list
ros2 topic info /topic --verbose
ros2 doctor
ping <ip-address>

⸻

Practical Lab Planned

Future exercise:

* Ubuntu laptop runs demo_nodes_cpp talker
* MacBook runs demo_nodes_cpp listener
* Verify DDS discovery
* Change ROS_DOMAIN_ID
* Observe communication failure
* Restore correct configuration
* Inspect QoS using ros2 topic info --verbose

⸻

Engineering Lessons

* Distributed robotics is about architecture, not just networking.
* ROS 2 eliminates the ROS Master using DDS peer-to-peer discovery.
* DDS performs discovery automatically before establishing direct communication.
* ROS_DOMAIN_ID provides logical isolation between robots.
* Most multi-machine ROS problems originate from networking or configuration rather than application code.
* Professional debugging starts from the network layer and progresses upward to the application layer.
* Real-world robotic systems distribute workloads across multiple computers to improve reliability, scalability, and maintainability.

⸻

Key Takeaways

✅ Understand why modern robots use multiple computers.

✅ Understand how DDS enables decentralized discovery.

✅ Configure and use ROS_DOMAIN_ID.

✅ Understand networking concepts required for ROS 2 deployment.

✅ Understand multicast-based discovery and direct data communication.

✅ Deploy ROS 2 across multiple machines.

✅ Apply a structured debugging workflow.

✅ Recognize production deployment architectures used in industrial robotics.

⸻

Self Evaluation

Conceptual Understanding: ★★★★★

Hands-on Coding: ★☆☆☆☆

System Architecture: ★★★★★

Networking Fundamentals: ★★★★☆

Deployment Readiness: ★★★★★

⸻

Next Module

Module 39 — Simulation & Digital Twin Engineering

Focus areas:

* Gazebo
* Digital Twins
* Physics Simulation
* Simulated Sensors
* Robot Control in Simulation
* Preparing the complete simulation environment for the 6-DOF robotic arm and future AUV projects.