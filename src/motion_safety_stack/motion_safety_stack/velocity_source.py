import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
class VelocitySource(Node):
    def __init__(self):
        super().__init__('velocity_source')
        self.cmd_vel_pub=self.create_publisher(
            Twist,
            '/cmd_vel_raw',
            10
        )
        self.obstacle_pub=self.create_publisher(
            Float32,
            '/obstacle_distance',
            10
        )
        self.get_logger().info(
            'Velocity Source Started'
        )
        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )
        self.state = 'accelerate'
        self.state_time = 0.0
        self.obstacle_distance = -1.0
        self.current_linear_speed = 0.0
    def timer_callback(self):
        self.state_time += 0.1
def main(args=None):
    rclpy.init(args=args)
    node = VelocitySource()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()        