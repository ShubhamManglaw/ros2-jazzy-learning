import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
class DescriptorNode(Node):
    def __init__(self):
        super().__init__("descriptor_node")
        descriptor = ParameterDescriptor(
            description="Maximum joint velocity in rad/s",
        )
        self.declare_parameter("max_velocity",1.0,descriptor)
        max_velocity = self.get_parameter("max_velocity").value
        self.get_logger().info(f"Maximum velocity: {max_velocity}")

def main(args=None):
    rclpy.init(args=args)
    node = DescriptorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()