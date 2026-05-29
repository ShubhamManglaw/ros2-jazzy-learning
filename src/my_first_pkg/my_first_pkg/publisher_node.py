import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):

    def __init__(self):
        super().__init__('simple_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'learning_topic',
            10
        )

        timer_period = 1.0

        self.timer = self.create_timer(
            timer_period,
            self.publish_message
        )

        self.counter = 0

    def publish_message(self):

        msg = String()

        msg.data = f'ROS2 Message #{self.counter}'

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing: "{msg.data}"'
        )

        self.counter += 1


def main(args=None):

    rclpy.init(args=args)

    node = SimplePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()