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
        self.obstacle_distance = 10.0
        self.current_linear_speed = 0.0
        self.side_count = 0
        self.acceleration_duration = 2.0
        self.straight_duration = 5.0
        self.corner_duration = 2.0
        self.declare_parameter('max_linear_speed', 0.0)
        self.declare_parameter('max_angular_speed', 0.0)
        self.declare_parameter('corner_linear_speed', 0.0)
        self.declare_parameter('corner_angular_speed', 0.0)
        self.declare_parameter('linear_speed_factor', 1.0)
        self.declare_parameter('angular_speed_factor', 1.0)
        self.max_linear_speed = self.get_parameter('max_linear_speed').value
        self.max_angular_speed = self.get_parameter('max_angular_speed').value
        self.corner_linear_speed = self.get_parameter('corner_linear_speed').value
        self.corner_angular_speed = self.get_parameter('corner_angular_speed').value
        self.linear_speed_factor = self.get_parameter('linear_speed_factor').value
        self.angular_speed_factor = self.get_parameter('angular_speed_factor').value
        self.straight_speed = (
            self.max_linear_speed *
            self.linear_speed_factor
        )

        self.turn_speed = (
            self.corner_linear_speed *
            self.linear_speed_factor
        )

        self.turn_rate = (
            self.corner_angular_speed *
            self.angular_speed_factor
        )
    def timer_callback(self):
        self.state_time += 0.1
        cmd = Twist()
        obstacle = Float32()
        if self.state=='accelerate':
            cmd.linear.x=1.75
            cmd.angular.z = 0.0
            if self.state_time>=self.acceleration_duration:
                self.state = 'straight'
                self.state_time = 0.0
                self.get_logger().info('Switching to straight')
        elif self.state == 'straight':
            cmd.linear.x = self.straight_speed
            cmd.angular.z = 0.0
            if self.state_time >= self.straight_duration:
                self.state = 'corner'
                self.state_time = 0.0
                self.get_logger().info('Switching to corner')
        elif self.state == 'corner':
            cmd.linear.x = self.turn_speed
            cmd.angular.z = self.turn_rate
            if self.state_time >= self.corner_duration:
                self.side_count += 1

                if self.side_count >= 4:
                    self.state = 'obstacle'
                    self.state_time = 0.0
                    self.get_logger().info(
                        'Entering obstacle phase'
                    )
                else:
                    self.state = 'straight'
                    self.state_time = 0.0
                    self.get_logger().info(
                        f'Completed side {self.side_count}'
                    )
                    self.get_logger().info(
                        f'Switching to straight (side {self.side_count + 1})'
                    )
        elif self.state == 'obstacle':
            cmd.linear.x = self.straight_speed
            cmd.angular.z = 0.0
            self.obstacle_distance -= 0.1
            
        self.obstacle_distance = max(
            self.obstacle_distance,
            0.0
        )
        obstacle.data = self.obstacle_distance
        self.cmd_vel_pub.publish(cmd)
        self.obstacle_pub.publish(obstacle)
        

def main(args=None):
    rclpy.init(args=args)
    node = VelocitySource()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()        