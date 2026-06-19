import rclpy
from rclpy.node import Node
from tf2_ros import Buffer
from tf2_ros import TransformListener
from tf2_ros import TransformException

class TfListener(Node):

    def __init__(self):
        super().__init__("tf_listener")
        self.buffer = Buffer()
        self.listener = TransformListener(
            self.buffer,
            self
        )
        self.timer = self.create_timer(
            1.0,
            self.lookup_transform
        )
    def lookup_transform(self):
        try:
            transform = self.buffer.lookup_transform(
                "odom",
                "base_link",
                rclpy.time.Time()
            )
            self.get_logger().info(
                f"x = {transform.transform.translation.x}"
            )
        except TransformException as ex:
            self.get_logger().warn(
                f"Transform unavailable: {ex}"
            )


def main():
    rclpy.init()
    node = TfListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()