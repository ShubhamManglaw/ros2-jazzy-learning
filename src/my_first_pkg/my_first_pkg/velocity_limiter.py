import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class VelocityLimiter(Node):
    def __init__(self):
        super().__init__('velocity_limiter')
        self.declare_parameter("max_linear_speed",0.5)
        self.declare_parameter("max_angular_speed",1.0)
        self.publisher_=self.create_publisher(Twist,'/cmd_vel',10)
        self.subscription=self.create_subscription(Twist,'/cmd_vel_raw',self.velocity_callback,10)
        self.get_logger().info("Velocity Limiter Started")
    def velocity_callback(self,msg):
        final=Twist()
        max_linear=self.get_parameter("max_linear_speed").value
        max_angular=self.get_parameter("max_angular_speed").value
        final.linear.x=max(-max_linear,min(msg.linear.x, max_linear))
        final.angular.z=max(-max_angular,min(msg.angular.z, max_angular))
        self.publisher_.publish(final)
        self.get_logger().info(
            f"Limits: linear={max_linear}, angular={max_angular}")
        self.get_logger().info(
            f'Final linear.x={final.linear.x}, angular.z={final.angular.z}')
def main(args=None):
    rclpy.init(args=args)
    node= VelocityLimiter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()