import rclpy
from rclpy.node import Node

class RobotInfo(Node):
    def __init__(self):
        super().__init__("robot_info")
        self.get_logger().info('Robot Info Node Started')
        self.declare_parameter(
            'robot_name',
            'unknown'
        )
        self.declare_parameter(
            'robot_type',
            'unknown'
        )
        self.declare_parameter( 
            'robot_weight_kg',
            0.0           
        )
        self.declare_parameter(
            'payload_capacity_kg',
            0.0
        )
        self.declare_parameter(
            'max_linear_speed',
            0.0
        )
        self.declare_parameter(
            'max_angular_speed',
            0.0
        )
        self.declare_parameter(
            'max_acceleration',
            0.0
        )
        self.declare_parameter(
            'stopping_distance',
            0.0
        )
        self.declare_parameter(
            'environment_name',
            'unknown'
        )
        self.declare_parameter(
            'linear_speed_factor',
            1.0
        )
        self.declare_parameter(
            'angular_speed_factor',
            1.0
        )
        self.declare_parameter(
            'acceleration_factor',
            1.0
        )
        self.declare_parameter(
            'stopping_distance_factor',
            1.0
        )
        self.robot_name=self.get_parameter('robot_name').value
        self.robot_type=self.get_parameter('robot_type').value
        self.robot_weight_kg=self.get_parameter('robot_weight_kg').value
        self.payload_capacity_kg=self.get_parameter('payload_capacity_kg').value
        self.max_linear_speed = self.get_parameter('max_linear_speed').value
        self.max_angular_speed = self.get_parameter('max_angular_speed').value
        self.max_acceleration = self.get_parameter('max_acceleration').value
        self.stopping_distance = self.get_parameter('stopping_distance').value
        self.environment_name = self.get_parameter('environment_name').value
        self.linear_speed_factor = self.get_parameter('linear_speed_factor').value
        self.angular_speed_factor = self.get_parameter('angular_speed_factor').value
        self.acceleration_factor = self.get_parameter('acceleration_factor').value
        self.stopping_distance_factor = self.get_parameter('stopping_distance_factor').value
        self.effective_linear_speed = (self.max_linear_speed *self.linear_speed_factor)
        self.effective_angular_speed = (self.max_angular_speed *self.angular_speed_factor)
        self.effective_acceleration = (self.max_acceleration *self.acceleration_factor)
        self.effective_stopping_distance = (self.stopping_distance *self.stopping_distance_factor)
        self.get_logger().info(f'Robot: {self.robot_name}')
        self.get_logger().info(f'Type: {self.robot_type}')
        self.get_logger().info(f'Environment: {self.environment_name}')
        self.get_logger().info(f'Effective Linear Speed: {self.effective_linear_speed:.2f}')
        self.get_logger().info(f'Effective Angular Speed: {self.effective_angular_speed:.2f}')
        self.get_logger().info(f'Effective Acceleration: {self.effective_acceleration:.2f}')
        self.get_logger().info(f'Effective Stopping Distance: {self.effective_stopping_distance:.2f}')




def main(args=None):
    rclpy.init(args=args)
    node = RobotInfo()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()