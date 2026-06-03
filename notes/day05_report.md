# Day 05 Report — Multi-Node Pipeline

## Status
✅ Completed

## Date
03 June 2026

## Planned Hours
3 Hours

## Actual Hours
4 Hours

## Confidence
9/10

---

# Objective

Build a complete ROS2 multi-node pipeline where data flows through multiple nodes using topics.

Pipeline:

number_publisher
↓
/number
↓
number_doubler
↓
/doubled_number
↓
number_printer

---

# Concepts Covered

- Multi-node ROS2 architecture
- Topic chaining
- Publisher nodes
- Subscriber nodes
- Processing nodes
- Event-driven callbacks
- Message flow between nodes
- ROS graph visualization
- Topic inspection tools
- Node inspection tools
- Int32 message communication
- Queue depth
- Callback execution

---

# Nodes Created

## 1. NumberPublisher

Responsibilities:

- Create publisher on `/number`
- Publish increasing integers
- Use timer callback every 1 second

Output:

0
1
2
3
4
...

---

## 2. NumberDoubler

Responsibilities:

- Subscribe to `/number`
- Receive Int32 messages
- Multiply received value by 2
- Publish result on `/doubled_number`

Example:

Input: 5
Output: 10

Logs:

5 -> 10

---

## 3. NumberPrinter

Responsibilities:

- Subscribe to `/doubled_number`
- Display received values

Example:

Received number: 10

---

# ROS Graph Built

number_publisher
│
└── /number
│
▼
number_doubler
│
└── /doubled_number
│
▼
number_printer

---

# Hands-On Build Tasks

### Task 1
Created `number_publisher.py`

Learned:

- create_publisher()
- create_timer()
- Int32 messages
- Logger usage

---

### Task 2
Created `number_doubler.py`

Learned:

- create_subscription()
- Callback execution
- Processing incoming messages
- Publishing transformed messages

---

### Task 3
Created `number_printer.py`

Learned:

- Subscriber-only node design
- Logging received messages

---

### Task 4
Updated setup.py

Added executables:

- number_publisher
- number_doubler
- number_printer

---

### Task 5
Built workspace

Commands used:

```bash
colcon build --packages-select my_first_pkg
source install/setup.bash