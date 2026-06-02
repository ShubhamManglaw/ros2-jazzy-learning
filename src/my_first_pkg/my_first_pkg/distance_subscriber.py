import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        self.subscription=self.create_subscription(
            String,
            'ultrasonic_distance',
            self.receive_distance,
            10
        )
    def receive_distance(self, msg):
        updated_distance = int(msg.data.split(" ")[2])

        if updated_distance > 50:
            self.get_logger().info(f"The Distance is {updated_distance} cm, which is     SAFE")

        elif updated_distance > 20:
            self.get_logger().info(f"The Distance is {updated_distance} cm, which is WARNING")

        else:
            self.get_logger().info(f"The Distance is {updated_distance} cm, which is STOP")
    
def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()