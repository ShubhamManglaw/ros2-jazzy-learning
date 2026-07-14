from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="namespace_demo",
            executable="status_publisher",
            name="status_publisher",
            namespace="arm1"
        ),
        Node(
            package="namespace_demo",
            executable="status_publisher",
            name="status_publisher",
            namespace="arm2"
        )
    ])