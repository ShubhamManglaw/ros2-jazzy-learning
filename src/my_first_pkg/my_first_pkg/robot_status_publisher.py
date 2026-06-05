import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import RobotStatus
class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(
            RobotStatus,
            'robot_status',
            10
        )
        self.timer = self.create_timer(

            1.0,

            self.publish_status

        )
    def publish_status(self):
        msg=RobotStatus()
        msg.battery_percentage=85.0
        msg.robot_mode = RobotStatus.MODE_AUTONOMOUS
        msg.emergency_stop = False
        msg.linear_velocity_mps = 0.5
        msg.angular_velocity_radps = 0.1
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Battery: {msg.battery_percentage}% Mode: {msg.robot_mode}'
        )
def main(args=None):

    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
