import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.distance = 120
        self.publisher_=self.create_publisher(
            String,
            'ultrasonic_distance',
            10
        )

        self.timer=self.create_timer(
            1.0,
            self.publish_distance
        )
    def publish_distance(self):
        msg=String()
        msg.data=f'Distance is {self.distance} cm'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        if self.distance > 0:
            self.distance-=1
        else:
            self.distance = 0
    
def main(args=None):
    rclpy.init(args=args)
    node=DistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()