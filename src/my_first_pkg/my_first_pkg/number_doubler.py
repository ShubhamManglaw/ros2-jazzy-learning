import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
class NumberDoubler(Node):
    def __init__(self):
        super().__init__('number_doubler')
        self.publisher_ = self.create_publisher(
            Int32,
            'doubled_number',
            10
        )
        self.subscription = self.create_subscription(
    Int32,
    'number',
    self.number_callback,
    10
)
    def number_callback(self, msg):
        out = Int32()
        out.data = msg.data * 2
        self.publisher_.publish(out)
        self.get_logger().info(
            f'{msg.data} -> {out.data}'
        )
def main(args=None):
    rclpy.init(args=args)
    node= NumberDoubler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
        