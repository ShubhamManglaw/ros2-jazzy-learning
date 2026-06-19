from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    broadcaster = Node(
        package="tf2_demo",
        executable="dynamic_broadcaster"
    )

    listener = Node(
        package="tf2_demo",
        executable="tf_listener"
    )

    return LaunchDescription([
        broadcaster,
        listener
    ])