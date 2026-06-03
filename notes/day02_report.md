# Day 02 Report – ROS 2 Workspace Deep Dive

## Date

June 2026

## Objective

Understand the ROS 2 workspace structure, package organization, build workflow, sourcing process, and ROS computation graph.

## Concepts Covered

### ROS Computation Graph

* Nodes
* Topics
* Publishers
* Subscribers
* Decoupled communication

### Workspace Structure

* src/
* build/
* install/
* log/

### Package Structure

* package.xml
* setup.py
* setup.cfg
* resource/
* Python package directory

### Build Workflow

* colcon build
* Incremental builds
* Package installation

### Environment Setup

* source /opt/ros/jazzy/setup.bash
* source install/setup.bash

### ROS CLI Tools

* ros2 pkg list
* ros2 pkg executables
* ros2 node list
* ros2 topic list

## Practical Work

Created and built the package:

my_first_pkg

Verified package visibility through ROS CLI commands.

Successfully ran publisher and subscriber nodes.

Explored the workspace directory structure using:

tree -L 3

## Problems Encountered

### Package Not Found Error

Error:

Package 'my_first_pkg' not found

Cause:
Workspace was not sourced after opening a new terminal.

Fix:

source install/setup.bash

### Build vs Source Confusion

Initially confused building a package with sourcing a workspace.

Learned that:

* Build creates install artifacts.
* Source loads them into the current terminal environment.

## Key Learnings

* ROS packages exist inside a workspace.
* Every terminal requires sourcing.
* Nodes communicate through topics.
* Publishers and subscribers do not know about each other directly.
* build/, install/, and log/ have different responsibilities.

## Commands Practiced

```bash
colcon build
source install/setup.bash
ros2 pkg list
ros2 pkg executables my_first_pkg
tree -L 3
```

## Outcome

Can confidently navigate a ROS 2 workspace, build packages, source environments, and understand the ROS computation graph.
