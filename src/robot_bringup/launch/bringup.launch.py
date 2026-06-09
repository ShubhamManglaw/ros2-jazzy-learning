from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
def generate_launch_description():
    config_file = PathJoinSubstitution([
        FindPackageShare('robot_bringup'),'config',
        LaunchConfiguration('profile')
    ])

    return LaunchDescription([
        DeclareLaunchArgument(
            'profile',
            default_value='indoor.yaml'
        ),

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