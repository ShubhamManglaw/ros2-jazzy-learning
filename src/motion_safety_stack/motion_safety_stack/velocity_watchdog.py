import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityWatchdog(Node):

    def __init__(self):
        super().__init__('velocity_watchdog')

        self.get_logger().info(
            'Velocity Watchdog Started'
        )

        self.declare_parameter(
            'timeout_seconds',
            2.0
        )

        self.declare_parameter(
            'watchdog_enabled',
            True
        )

        self.timeout_seconds = (
            self.get_parameter(
                'timeout_seconds'
            ).value
        )

        self.watchdog_enabled = (
            self.get_parameter(
                'watchdog_enabled'
            ).value
        )

        self.current_cmd = Twist()

        self.last_message_time = (
            self.get_clock().now()
        )

        self.timeout_triggered = False

        self.cmd_sub = self.create_subscription(
            Twist,
            '/cmd_vel_safe',
            self.cmd_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

    def cmd_callback(self, msg):

        self.current_cmd = msg

        self.last_message_time = (
            self.get_clock().now()
        )

        self.timeout_triggered = False

    def timer_callback(self):

        elapsed = (
            self.get_clock().now()
            - self.last_message_time
        ).nanoseconds / 1e9

        if (
            self.watchdog_enabled
            and
            elapsed > self.timeout_seconds
        ):

            stop_cmd = Twist()

            self.cmd_pub.publish(
                stop_cmd
            )

            if not self.timeout_triggered:

                self.get_logger().warn(
                    f'Watchdog timeout! '
                    f'No command for '
                    f'{elapsed:.2f}s'
                )

            self.timeout_triggered = True

        else:

            self.cmd_pub.publish(
                self.current_cmd
            )

def main(args=None):

    rclpy.init(args=args)

    node = VelocityWatchdog()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()