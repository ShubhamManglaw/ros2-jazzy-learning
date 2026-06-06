import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_callback
        )
        self.get_logger().info('AddTwoInts Service Server Ready')
    def add_callback(self,request,responce):
        responce.sum=request.a +request.b
        self.get_logger().info(

            f'Request: {request.a} + {request.b} = {responce.sum}'

        )
        return responce


def main(args=None):

    rclpy.init(args=args)

    node = AddTwoIntsServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':

    main()
