from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory(
            "my_robot_description"
        ),
        "urdf",
        "my_robot.urdf"
    )
    with open(urdf_file, "r") as file:
        robot_description = file.read()

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": robot_description}]
        ),
        Node(
            package="rviz2",
            executable="rviz2",

        )
    ])
    