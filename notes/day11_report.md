# Day 11 Report — Service Server

## Objective

Build and run a ROS 2 Service Server capable of receiving requests, processing data, and returning responses.

---

## Concepts Covered

- Service Server Architecture
- create_service()
- Service Callback Functions
- Request Objects
- Response Objects
- AddTwoInts Service
- Service Discovery
- Service Testing with CLI

---

## Implementation

Created:

text src/my_first_pkg/my_first_pkg/add_server.py 

Implemented a ROS 2 Service Server using:

python from example_interfaces.srv import AddTwoInts 

Service name:

text /add_two_ints 

Service type:

text example_interfaces/srv/AddTwoInts 

---

## Callback Logic

The callback receives:

python request response 

and performs:

python response.sum = request.a + request.b 

before returning:

python return response 

---

## Package Updates

### package.xml

Added dependency:

xml <depend>example_interfaces</depend> 

### setup.py

Added executable:

python 'add_server = my_first_pkg.add_server:main' 

---

## Build Process

bash colcon build --packages-select my_first_pkg 

Result:

text Finished <<< my_first_pkg 

---

## Running the Server

bash ros2 run my_first_pkg add_server 

Output:

text AddTwoInts Service Server Ready 

---

## Service Verification

### List Services

bash ros2 service list | grep add 

Output:

text / add_two_ints 

### Check Service Type

bash ros2 service type /add_two_ints 

Output:

text example_interfaces/srv/AddTwoInts 

### Test Service

bash ros2 service call \ /add_two_ints \ example_interfaces/srv/AddTwoInts \ "{a: 10, b: 5}" 

Response:

text sum: 15 

Server Log:

text Request: 10 + 5 = 15 

---

## Challenges Encountered

- Forgot to declare example_interfaces dependency initially
- Mixed response variable naming during callback development
- Learned the importance of returning the response object

---

## Key Learnings

- Service Servers wait for requests.
- Service callbacks process incoming requests.
- Request and Response are separate objects.
- create_service() registers a service on the ROS graph.
- rclpy.spin() keeps the server alive and responsive.
- CLI tools are extremely useful for service debugging.

---

## Outcome

By the end of Day 11, I was able to:

- Build a ROS 2 Service Server
- Register services using create_service()
- Process client requests
- Return structured responses
- Verify services using ROS 2 CLI tools
- Debug service communication

---

## Reflection

Day 11 was the first implementation-focused service lesson. Unlike Day 10, which focused on concepts, this session involved building a functioning service server and validating the complete request-response cycle. This forms the foundation for Day 12, where a custom Service Client will be implemented to communicate with the server programmatically.