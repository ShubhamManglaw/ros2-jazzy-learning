import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
class NumberPrinter(Node):
    def __init__(self):
        super().__init__('number_printer')
        self.subscription = self.create_subscription(
            Int32,
            'doubled_number',
            self.number_callback,
            10
        )
    def number_callback(self, msg):
        self.get_logger().info(
            f'Received number: {msg.data}'
        )
def main(args=None):
    rclpy.init(args=args)
    node= NumberPrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()