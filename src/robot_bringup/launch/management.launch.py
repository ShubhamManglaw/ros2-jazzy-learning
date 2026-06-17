from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.actions import LogInfo
from launch.event_handlers import OnProcessStart
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    robot_namespace = LaunchConfiguration(
    "robot_namespace"
)
    managed_node = Node(
            package="lifecycle_demo",
            executable='lifecycle_node',
            name='managed_node',
            namespace=robot_namespace
        )
    node_started_handler = RegisterEventHandler(
        OnProcessStart(
            target_action=managed_node,
            on_start=[
                LogInfo(
                    msg="managed_node has started"
                )
            ]
        )
    )
    return LaunchDescription([
        managed_node,
        node_started_handler
        
    ])