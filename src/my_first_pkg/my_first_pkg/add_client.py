import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.client=self.create_client(
            AddTwoInts,
            'add_two_ints'
        )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(

                'service not available, waiting again...'

            )
        self.request = AddTwoInts.Request()
    def send_request(self,a,b):
        self.request.a = a
        self.request.b = b
        return self.client.call_async(self.request)


def main(args=None):
    rclpy.init(args=args)

    node = AddTwoIntsClient()
    future = node.send_request(10, 5)

    rclpy.spin_until_future_complete(node, future)
    response = future.result()
    node.get_logger().info(

        f"Result: {response.sum}"

    )
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':

    main()

