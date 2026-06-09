from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    bringup_dir = get_package_share_directory('robot_bringup')
    profile = LaunchConfiguration('profile')
    config_file = os.path.join(
        bringup_dir,
        'config',
        'indoor.yaml'
    )

    return LaunchDescription([
        DeclareLaunchArgument('profile',default_value='indoor'),
        Node(
            package='my_first_pkg',
            executable='velocity_source'
        ),
        Node(
            package='my_first_pkg',
            executable='velocity_limiter_v3',
            parameters=[config_file]
        ),
        Node(
            package='my_first_pkg',
            executable='velocity_monitor'
        )

    ])