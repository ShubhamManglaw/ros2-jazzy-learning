# Day 10 Report — Service Concept

## Objective

Understand ROS 2 Services, request-response communication, and when Services should be used instead of Topics.

---

## Concepts Covered

- ROS 2 Service Fundamentals
- Request–Response Communication
- Service Client
- Service Server
- Service Discovery
- Service Names vs Service Types
- Service Interfaces (.srv)
- Empty Services
- Topic vs Service Communication

---

## Hands-On Activities

### Started turtlesim

bash ros2 run turtlesim turtlesim_node 

### Listed available services

bash ros2 service list 

Observed services:

text /clear /kill /reset /spawn /turtle1/set_pen /turtle1/teleport_absolute /turtle1/teleport_relative 

### Inspected service interface

bash ros2 interface show std_srvs/srv/Empty 

Output:

text --- 

This demonstrated a service with no request fields and no response fields.

### Called a service manually

bash ros2 service call /clear std_srvs/srv/Empty 

Response:

text std_srvs.srv.Empty_Response() 

### Verified service execution

Turtlesim log:

text [turtlesim]: Clearing turtlesim. 

---

## Key Learnings

### Topics

- Publisher → Subscriber
- Continuous communication
- No response expected

Examples:

- Camera images
- LiDAR scans
- Odometry
- Battery status

### Services

- Client → Server
- Request → Response
- Response required

Examples:

- Reset odometry
- Save map
- Trigger calibration
- Enable/disable functionality

---

## Service Structure

text Request --- Response 

Example:

text int64 a int64 b --- int64 sum 

---

## Challenges Encountered

- Initially expected a visual change after calling /clear
- Confused Service Name and Service Type
- Needed server logs to verify successful execution

---

## Outcome

By the end of Day 10, I was able to:

- Explain ROS 2 Services
- Differentiate Topics and Services
- Inspect service interfaces
- Discover active services
- Invoke services from the command line
- Understand request-response communication

---

## Reflection

Day 10 introduced the second major ROS 2 communication mechanism after Topics. Services provide deterministic request-response communication and are ideal for commands, queries, and one-time operations. Understanding this distinction is important for designing scalable robotic systems.