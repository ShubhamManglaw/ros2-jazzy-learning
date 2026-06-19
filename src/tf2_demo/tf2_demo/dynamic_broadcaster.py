import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
class DynamicBroadcaster(Node):
    def __init__(self):
        super().__init__("dynamic_broadcaster")
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.publish_transform)
        self.x = 0.0
    def publish_transform(self):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_link"
        self.x += 0.1
        transform.transform.translation.x = self.x
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.0

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0
        self.tf_broadcaster.sendTransform(transform)

def main():
    rclpy.init()
    node = DynamicBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()