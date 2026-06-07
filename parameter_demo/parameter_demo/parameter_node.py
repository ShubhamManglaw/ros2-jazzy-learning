import rclpy
from rclpy.node import Node
class ParameterNode(Node):
    def __init__(self):
        super().__init__("parameter_node")
        self.declare_parameter("robot_name", "NewtonBot")
        self.declare_parameter("max_speed", 1.0)

        self.declare_parameter("battery_capacity", 100)
        robot_name = self.get_parameter(
            "robot_name"
        ).value

        max_speed = self.get_parameter(
            "max_speed"
        ).value

        battery = self.get_parameter(
            "battery_capacity"
        ).value
        self.get_logger().info(
    f"{robot_name} | Speed={max_speed} | Battery={battery}"
)
def main(args=None):

    rclpy.init(args=args)

    node = ParameterNode()

    rclpy.spin_once(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":

    main()