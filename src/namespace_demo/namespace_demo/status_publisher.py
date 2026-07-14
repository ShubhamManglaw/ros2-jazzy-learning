import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class StatusPublisher(Node):
    def __init__(self):
        super().__init__("status_publisher")
        self.status_publisher = self.create_publisher(
            String,
            "status",
            10
        )
        self.timer=self.create_timer(1.0,self.timer_callback)
    def timer_callback(self):
        msg=String()
        msg.data="Robot is operational."
        self.status_publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
