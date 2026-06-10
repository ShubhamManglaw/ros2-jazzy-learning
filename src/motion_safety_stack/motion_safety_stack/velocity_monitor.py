import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
class VelocityMonitor(Node):
    def __init__(self):
        super().__init__('velocity_monitor')
        self.get_logger().info('Velocity Monitor Started')
        self.raw_cmd = Twist()
        self.limited_cmd = Twist()
        self.obstacle_distance = -1.0
        self.cmd_vel_raw_sub = self.create_subscription(Twist,'/cmd_vel_raw',self.cmd_vel_raw_callback,10)
        self.cmd_vel_sub = self.create_subscription(Twist,'/cmd_vel',self.cmd_vel_callback,10)
        self.obstacle_sub=self.create_subscription(Float32,'/obstacle_distance',self.obstacle_callback,10)
        self.timer = self.create_timer(1.0,self.timer_callback)

    def cmd_vel_raw_callback(self, msg):
        self.raw_cmd = msg

    def cmd_vel_callback(self, msg):
        self.limited_cmd = msg

    def obstacle_callback(self, msg):
        self.obstacle_distance = msg.data
    def timer_callback(self):
        braking=(self.limited_cmd.linear.x<self.raw_cmd.linear.x)
        self.get_logger().info(
                    f'Raw: {self.raw_cmd.linear.x:.2f} | '
                    f'Limited: {self.limited_cmd.linear.x:.2f} | '
                    f'Obstacle: {self.obstacle_distance:.2f} m | '
                    f'Braking: {braking}'
        )
def main(args=None):
    rclpy.init(args=args)
    node= VelocityMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()