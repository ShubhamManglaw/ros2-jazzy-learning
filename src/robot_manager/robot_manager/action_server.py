import time
import rclpy
from rclpy.node import Node
from rclpy.action import (ActionServer,CancelResponse)
from my_robot_interfaces.action import NavigateToPose
class NavigateToPoseServer(Node):
    def __init__(self):
        super().__init__('navigate_to_pose_server')
        self._action_server=ActionServer(
            self,
            NavigateToPose,
            'navigate_to_pose',
            execute_callback=self.execute_callback,
            cancel_callback=self.cancel_callback
        )
    def cancel_callback(self, goal_handle):
        self.get_logger().info(
            "Cancel request received"
        )
        return CancelResponse.ACCEPT
    def execute_callback(self,goal_handle):
        x=goal_handle.request.x
        y=goal_handle.request.y
        yaw=goal_handle.request.yaw
        self.get_logger().info(
            f"Received goal: x={x}, y={y}, yaw={yaw}"
        )
        feedback_msg = NavigateToPose.Feedback()
        distance_remaining = 5.0
        while distance_remaining > 0:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info(
                   "Goal canceled"
                )
                result = NavigateToPose.Result()
                result.success = False
                result.message = "Navigation canceled"
                return result
            feedback_msg.distance_remaining = distance_remaining
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(
                f"Distance Remaining: {distance_remaining}"
            )
            distance_remaining -= 1.0
            time.sleep(1)
        goal_handle.succeed()
        result=NavigateToPose.Result()
        result.success = True
        result.message="Navigation completed"
        return result

def main(args=None):
    rclpy.init(args=args)
    node = NavigateToPoseServer()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()