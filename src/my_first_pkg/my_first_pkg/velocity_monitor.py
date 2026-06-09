import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class VelocityMonitor(Node):
    def __init__(self):
        super().__init__('velocity_monitor')
        self.log_counter = 0
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.velocity_callback,
            10
        )
    def velocity_callback(self,msg):
        self.log_counter += 1
        if self.log_counter % 5 == 0:
            self.get_logger().info(
                f"Received: linear.x={msg.linear.x}, angular.z={msg.angular.z}"
                )

def main(args=None):
    rclpy.init(args=args)
    node= VelocityMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
