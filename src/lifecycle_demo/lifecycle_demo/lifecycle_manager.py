import rclpy

from rclpy.node import Node
from lifecycle_msgs.srv import ChangeState

class LifecycleManager(Node):

    def __init__(self):
        super().__init__('lifecycle_manager')

        self.get_logger().info(
            'Lifecycle manager started'
        )
        self.change_state_client = self.create_client(
            ChangeState,
            '/lifecycle_node/change_state'
        )
        while not self.change_state_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for lifecycle node...'
            )
    def configure_node(self):
        request = ChangeState.Request()
        request.transition.id = 1
        self.get_logger().info(
            'Sending configure request'
        )
        future = self.change_state_client.call_async(
            request
        )
        rclpy.spin_until_future_complete(
            self,
            future
        )
        response = future.result()
        self.get_logger().info(
            f'Configure success: {response.success}'
        )
        
    def activate_node(self):
        request = ChangeState.Request()
        request.transition.id = 3
        self.get_logger().info(
            'Sending activate request'
        )
        future = self.change_state_client.call_async(
            request
        )
        rclpy.spin_until_future_complete(
            self,
            future
        )
        response = future.result()
        self.get_logger().info(
            f'Activate success: {response.success}'
        )
def main(args=None):
    rclpy.init(args=args)
    manager = LifecycleManager()
    manager.configure_node()
    manager.activate_node()
    manager.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    