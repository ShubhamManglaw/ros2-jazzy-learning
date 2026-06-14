import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_robot_interfaces.action import NavigateToPose
class NavigateToPoseClient(Node):
    def __init__(self):
        super().__init__('navigate_to_pose_client')
        self._action_client = ActionClient(
            self,
            NavigateToPose,
            'navigate_to_pose'
        )
    def send_goal(self):
        goal_msg = NavigateToPose.Goal()
        goal_msg.x = 5.0
        goal_msg.y = 2.0
        goal_msg.yaw = 1.5
        self._action_client.wait_for_server()
        self.get_logger().info("Sending navigation goal")
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(
            self.goal_response_callback
        )
    def goal_response_callback(self, future):
        self._goal_handle = future.result()
        if not self._goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        self.get_logger().info("Goal Accepted")
        self.cancel_timer = self.create_timer(
            2.0,
            self.cancel_goal
        )
        self._get_result_future = (
            self._goal_handle.get_result_async()
        )
        self._get_result_future.add_done_callback(
            self.get_result_callback
        )
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f"Distance Remaining: {feedback.distance_remaining}"
        )
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(
            f"Success: {result.success}"
        )
        self.get_logger().info(
            f"Message: {result.message}"
        )
    def cancel_goal(self):
        self.cancel_timer.cancel()
        self.get_logger().info(
            "Requesting goal cancellation"
        )
        self._cancel_future = (
            self._goal_handle.cancel_goal_async()
        )
        self._cancel_future.add_done_callback(
            self.cancel_done_callback
        )
    def cancel_done_callback(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) == 0:
            self.get_logger().info(
                "Goal cancellation rejected"
            )
        else:
            self.get_logger().info(
                "Goal cancellation accepted"
            )
def main(args=None):
    rclpy.init(args=args)
    node = NavigateToPoseClient()
    node.send_goal()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()