import rclpy
from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle import TransitionCallbackReturn
from std_msgs.msg import String

class LifecycleDemoNode(LifecycleNode):
    def __init__(self):
        super().__init__('lifecycle_node')
        self.get_logger().info(
            'Lifecycle node created'
        )
        self.publisher_ = None
        self.timer_ = None
    def on_configure(self, state):
        self.get_logger().info(
            'Configuring node...'
        )
        self.publisher_ = self.create_lifecycle_publisher(
            String,
            'lifecycle_chatter',
            10
        )
        self.timer_ = self.create_timer(
            1.0,
            self.timer_callback
        )
        self.get_logger().info(
            'Configuration complete'
        )
        return TransitionCallbackReturn.SUCCESS
    def on_activate(self, state):
        self.get_logger().info(
            'Activating node...'
        )
        super().on_activate(state)
        self.get_logger().info(
            'Node is active'
        )
        return TransitionCallbackReturn.SUCCESS
    def on_deactivate(self, state):
        self.get_logger().info(
            'Deactivating node...'
        )
        super().on_deactivate(state)
        self.get_logger().info(
            'Node is inactive'
        )
        return TransitionCallbackReturn.SUCCESS
    def on_cleanup(self, state):
        self.get_logger().info(
            'Cleaning up resources...'
        )
        self.publisher_ = None
        if self.timer_ is not None:
            self.destroy_timer(self.timer_)
            self.timer_ = None
        return TransitionCallbackReturn.SUCCESS
    def on_shutdown(self, state):
        self.get_logger().info(
            'Shutting down node...'
        )
        return TransitionCallbackReturn.SUCCESS
    def on_error(self, state):
        self.get_logger().error(
            'Lifecycle error detected'
        )
        return TransitionCallbackReturn.SUCCESS
    def timer_callback(self):
        if self.publisher_ is None:
            return
        msg = String()
        msg.data = "Lifecycle node running"
        self.publisher_.publish(msg)
        self.get_logger().info(
            msg.data
        )
def main(args=None):
    rclpy.init(args=args)
    node= LifecycleDemoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()


