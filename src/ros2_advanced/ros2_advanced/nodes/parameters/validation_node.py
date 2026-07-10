import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
from rcl_interfaces.msg import SetParametersResult

class ValidationNode(Node):
    def __init__(self):
        super().__init__("validation_node")
        descriptor = ParameterDescriptor(
            description="Maximum joint velocity in rad/s",
        )
        self.declare_parameter("max_velocity",1.0,descriptor)
        max_velocity = self.get_parameter("max_velocity").value
        self.add_on_set_parameters_callback(
            self.parameter_callback
        )
        self.get_logger().info(f"Maximum velocity: {max_velocity}")
    def parameter_callback(self,parameters):
        result = SetParametersResult()
        result.successful = True
        for parameter in parameters:
            if parameter.name == "max_velocity":
                if parameter.value <= 0.0 or parameter.value > 10.0:
                    result.successful = False
                    result.reason = "Maximum velocity must be between 0 and 10"
                else:
                    self.get_logger().info(f"Maximum velocity updated to {parameter.value}")
                    result.successful = True
        return result

def main(args=None):
    rclpy.init(args=args)
    node = ValidationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()