from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    robot_namespace = LaunchConfiguration(
        "robot_namespace"
    )
    return LaunchDescription([
        Node(
            package="my_first_pkg",
            executable='velocity_source',
            name='navigation_node',
            namespace=robot_namespace
        )
    ])