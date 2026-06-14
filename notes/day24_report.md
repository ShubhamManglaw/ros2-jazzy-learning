Day 24 Report — Action Architecture Engineering

Objective

Learn and implement ROS 2 Actions by building a complete Action Client–Server architecture using a custom NavigateToPose action interface. Understand goal handling, feedback publishing, result generation, and cancellation mechanisms used in long-running robotic tasks.

⸻

Concepts Learned

Why Actions Exist

Services are suitable for short request-response interactions but become inefficient for long-running tasks. Actions solve this problem by providing:

* Goal submission
* Continuous feedback
* Final result reporting
* Goal cancellation

Typical robotics use cases include:

* Navigation
* Manipulation
* Inspection
* Autonomous missions

⸻

Action Structure

A ROS 2 Action consists of three sections:

Goal
---
Result
---
Feedback

Implemented Action:

float64 x
float64 y
float64 yaw
---
bool success
string message
---
float64 distance_remaining

⸻

Action Client Responsibilities

* Send goals
* Receive goal acceptance/rejection
* Receive feedback
* Receive final result
* Request goal cancellation

Action Server Responsibilities

* Accept goals
* Execute tasks
* Publish feedback
* Return results
* Handle cancellation requests

⸻

Implementation

Custom Action Interface

Used the custom action:

my_robot_interfaces/action/NavigateToPose

Verified using:

ros2 interface show my_robot_interfaces/action/NavigateToPose

⸻

Action Server

Implemented:

ActionServer(
    self,
    NavigateToPose,
    'navigate_to_pose',
    execute_callback=self.execute_callback,
    cancel_callback=self.cancel_callback
)

Server functionality:

* Receives navigation goals
* Publishes distance remaining feedback
* Returns success result
* Handles cancellation requests

⸻

Action Client

Implemented:

ActionClient(
    self,
    NavigateToPose,
    'navigate_to_pose'
)

Client functionality:

* Sends navigation goal
* Processes goal response
* Receives feedback updates
* Receives final result
* Sends cancellation request

⸻

Verification Performed

Action Discovery

ros2 action list

Output:

/navigate_to_pose

⸻

Action Information

ros2 action info /navigate_to_pose

Output:

Action: /navigate_to_pose
Action servers: 1

⸻

Node Discovery

ros2 node list

Output:

/navigate_to_pose_server
/navigate_to_pose_client

⸻

Interface Verification

ros2 interface show my_robot_interfaces/action/NavigateToPose

Successfully verified Goal, Result, and Feedback sections.

⸻

Action Flow Implemented

Client
   │
   ▼
Send Goal
   │
   ▼
Goal Accepted
   │
   ▼
Feedback Published
   │
   ▼
Result Returned

⸻

Cancellation Flow Implemented

Goal Running
   │
   ▼
Cancel Request Sent
   │
   ▼
Cancel Callback Triggered

Client-side cancellation request logic and response handling were implemented successfully. Server-side cancellation architecture was implemented and explored as part of Action lifecycle learning.

⸻

Key ROS 2 APIs Learned

Client Side

send_goal_async()
get_result_async()
cancel_goal_async()

Server Side

ActionServer()
publish_feedback()
goal_handle.succeed()
goal_handle.canceled()

⸻

Challenges Encountered

* Understanding Goal, Feedback, and Result generated classes
* Understanding asynchronous callback flow
* Managing GoalHandle lifecycle
* Implementing cancellation requests
* Debugging Action discovery and execution behavior

⸻

Outcome

Successfully built and verified a complete ROS 2 Action Client–Server architecture using a custom action interface. Learned the full Action lifecycle including goal submission, feedback publishing, result handling, action discovery, and cancellation mechanisms. Gained practical understanding of how ROS 2 Actions are used in production robotics frameworks such as Navigation2.

⸻

Commands Used

ros2 action list
ros2 action info /navigate_to_pose
ros2 node list
ros2 interface show my_robot_interfaces/action/NavigateToPose
ros2 run robot_manager action_server
ros2 run robot_manager action_client

⸻

Status

✅ Day 24 Completed

Topics Mastered:

* ROS 2 Actions
* Goal Handling
* Feedback Handling
* Result Handling
* Action Client Architecture
* Action Server Architecture
* Action Discovery Tools
* Cancellation Concepts