# Day 12 Report — Service Client

## Objective

Build a ROS 2 Service Client capable of sending requests to a Service Server and receiving responses asynchronously.

---

## Concepts Covered

- Service Client Architecture
- create_client()
- wait_for_service()
- Request Objects
- Future Objects
- call_async()
- spin_until_future_complete()
- Client-Server Communication
- Service Availability Checking

---

## Implementation

Created:

text src/my_first_pkg/my_first_pkg/add_client.py 

Implemented a ROS 2 Service Client using:

python from example_interfaces.srv import AddTwoInts 

Connected to:

text /add_two_ints 

Service type:

text example_interfaces/srv/AddTwoInts 

---

## Client Design

### Create Client

python self.client = self.create_client(     AddTwoInts,     'add_two_ints' ) 

This creates a client for the existing AddTwoInts service.

---

### Wait For Service

python while not self.client.wait_for_service(timeout_sec=1.0):     self.get_logger().info(         'service not available, waiting again...'     ) 

Purpose:

- Prevent client startup failures
- Wait until the server becomes available
- Improve reliability

---

### Create Request

python self.request = AddTwoInts.Request() 

Request fields:

text a b 

Values assigned:

python self.request.a = a self.request.b = b 

---

### Send Request

python future = self.client.call_async(self.request) 

Key concept:

A Future represents a result that will arrive later.

---

### Wait For Response

python rclpy.spin_until_future_complete(     node,     future ) 

This blocks execution until the service response arrives.

---

### Read Response

python response = future.result() 

Result used:

python response.sum 

---

## Package Updates

### setup.py

Added executable:

python 'add_client = my_first_pkg.add_client:main' 

---

## Build Process

bash colcon build --packages-select my_first_pkg 

Build completed successfully.

---

## Running the System

### Terminal 1

bash ros2 run my_first_pkg add_server 

Output:

text AddTwoInts Service Server Ready 

### Terminal 2

bash ros2 run my_first_pkg add_client 

Output:

text Result: 15 

---

## Communication Verification

Client sent:

text a = 10 b = 5 

Server processed:

text 10 + 5 = 15 

Server log:

text Request: 10 + 5 = 15 

Client received:

text Result: 15 

---

## Debugging / Mistakes

### Issue 1

Forgot the first parameter of a class method.

Incorrect:

python def send_request(a, b): 

Correct:

python def send_request(self, a, b): 

Reason:

Class methods must receive self.

---

### Issue 2

Forgot to create the Future.

Incorrect:

python rclpy.spin_until_future_complete(     node,     future ) 

without defining future.

Correct:

python future = node.send_request(10, 5) 

---

### Issue 3

Forgot to retrieve the response.

Correct:

python response = future.result() 

---

## Key Learnings

- Service Clients initiate communication.
- Service Servers respond to requests.
- create_client() connects to a service.
- wait_for_service() improves robustness.
- call_async() returns a Future.
- Future objects represent pending results.
- spin_until_future_complete() waits for responses.
- Client and Server must share the same service name and service type.

---

## Outcome

By the end of Day 12, I was able to:

- Build a ROS 2 Service Client
- Connect to a Service Server
- Create request objects
- Send asynchronous service requests
- Handle Future objects
- Retrieve responses
- Verify full client-server communication

---

## Comparison With Day 11

Day 11:

text Service Server Receives requests Returns responses 

Day 12:

text Service Client Creates requests Receives responses 

Together they form a complete ROS 2 Service system.

---

## Reflection

Day 12 completed the request-response communication model in ROS 2. Building the Service Client provided a deeper understanding of asynchronous communication, Futures, and service availability. The successful interaction between add_client and add_server demonstrated the full ROS 2 service workflow and established a foundation for more advanced communication patterns such as custom services and actions.

---

## Completion Evidence

Server Output:

text [add_two_ints_server]: Request: 10 + 5 = 15 

Client Output:

text [add_two_ints_client]: Result: 15 

Status: Completed
Confidence: High
Independent Build Score: 8.5/10