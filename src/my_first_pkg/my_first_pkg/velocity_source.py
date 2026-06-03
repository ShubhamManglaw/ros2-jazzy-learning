import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class VelocitySource(Node):
    def __init__(self):
        super().__init__('velocity_source')
        self.publisher_ = self.create_publisher(
            Twist,
            '/cmd_vel_raw',
            10
        )
        self.timer = self.create_timer(
            1.0,
            self.publish_velocity
        )
    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.5
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'linear.x={msg.linear.x}, angular.z={msg.angular.z}'
        )
def main(args=None):
    rclpy.init(args=args)
    node= VelocitySource()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()