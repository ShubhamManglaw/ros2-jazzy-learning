import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class VelocityLimiter(Node):
    def __init__(self):
        super().__init__('velocity_limiter')
        self.publisher_=self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )
        self.subscription=self.create_subscription(
            Twist,
            '/cmd_vel_raw',
            self.velocity_callback,
            10
        )
    def velocity_callback(self,msg):
        final=Twist()
        final.linear.x = max(-0.5, min(msg.linear.x, 0.5))
        final.angular.z = max(-1.0, min(msg.angular.z, 1.0))
        self.publisher_.publish(final)
        self.get_logger().info(
            f'Final linear.x={final.linear.x}, angular.z={final.angular.z}'
        )
def main(args=None):
    rclpy.init(args=args)
    node= VelocityLimiter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()