import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
class VelocityLimiter(Node):
    def __init__(self):
        super().__init__('velocity_limiter')
        self.get_logger().info('Velocity Limiter Started')
        self.cmd_vel_sub=self.create_subscription(Twist,'/cmd_vel_raw',self.cmd_vel_callback,10)
        self.obstacle_sub=self.create_subscription(Float32,'/obstacle_distance',self.obstacle_callback,10)
        self.cmd_vel_pub=self.create_publisher(Twist,'/cmd_vel',10)
        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )
        self.current_cmd = Twist()
        self.obstacle_distance = -1.0
        self.current_linear_speed = 0.0
        self.dt = 0.1
        self.max_deceleration = 1.0
        self.declare_parameter('max_linear_speed', 0.0)
        self.declare_parameter('max_angular_speed', 0.0)
        self.declare_parameter('max_acceleration', 0.0)
        self.declare_parameter('stopping_distance', 0.0)
        self.declare_parameter('linear_speed_factor', 1.0)
        self.declare_parameter('angular_speed_factor', 1.0)
        self.declare_parameter('acceleration_factor', 1.0)
        self.declare_parameter('stopping_distance_factor', 1.0)
        self.max_linear_speed = self.get_parameter('max_linear_speed').value
        self.max_angular_speed = self.get_parameter('max_angular_speed').value
        self.max_acceleration = self.get_parameter('max_acceleration').value
        self.stopping_distance = self.get_parameter('stopping_distance').value
        self.linear_speed_factor = self.get_parameter('linear_speed_factor').value
        self.angular_speed_factor = self.get_parameter('angular_speed_factor').value
        self.acceleration_factor = self.get_parameter('acceleration_factor').value
        self.stopping_distance_factor = self.get_parameter('stopping_distance_factor').value
        self.max_linear_speed = (self.max_linear_speed *self.linear_speed_factor)
        self.max_angular_speed = (self.max_angular_speed *self.angular_speed_factor)
        self.max_acceleration = (self.max_acceleration *self.acceleration_factor)
        self.stopping_distance = (self.stopping_distance *self.stopping_distance_factor)
        self.declare_parameter('max_deceleration', 0.0)
        self.declare_parameter('deceleration_factor', 1.0)
        self.max_deceleration = self.get_parameter('max_deceleration').value
        self.deceleration_factor = self.get_parameter('deceleration_factor').value
        self.max_deceleration = (self.max_deceleration *self.deceleration_factor)
        self.get_logger().info(f'Effective Linear Speed: {self.max_linear_speed:.2f}')
        self.get_logger().info(f'Effective Angular Speed: {self.max_angular_speed:.2f}')
        self.get_logger().info(f'Effective Acceleration: {self.max_acceleration:.2f}')
        self.get_logger().info(f'Effective Stopping Distance: {self.stopping_distance:.2f}')
    def cmd_vel_callback(self, msg):
        self.current_cmd = msg
    def obstacle_callback(self, msg):
        self.obstacle_distance = msg.data
    def timer_callback(self):
        limited_cmd = Twist()
        if(self.obstacle_distance>=0.0 and self.obstacle_distance<=self.stopping_distance):
            target_speed=0.0
        else:
            target_speed=min(self.current_cmd.linear.x,self.max_linear_speed)
        if target_speed > self.current_linear_speed:
            max_delta = self.max_acceleration * self.dt
        else:
            max_delta = self.max_deceleration * self.dt
        if target_speed > self.current_linear_speed:
            self.current_linear_speed = min(self.current_linear_speed + max_delta,target_speed)
        elif target_speed < self.current_linear_speed:
            self.current_linear_speed = max(self.current_linear_speed - max_delta,target_speed)
        limited_cmd.linear.x = self.current_linear_speed
        limited_cmd.angular.z = max(min(self.current_cmd.angular.z,self.max_angular_speed),-self.max_angular_speed)
        self.cmd_vel_pub.publish(limited_cmd)
def main(args=None):
    rclpy.init(args=args)
    node = VelocityLimiter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()