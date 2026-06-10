from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (LaunchConfiguration,PathJoinSubstitution,PythonExpression,)
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
def generate_launch_description():
    robot = LaunchConfiguration('robot')
    environment = LaunchConfiguration('environment')
    package_share = FindPackageShare('motion_safety_stack')
    robot_config = PathJoinSubstitution([
        package_share,
        'config',
        'robots',
        PythonExpression([
            "'",
            robot,
            "' + '.yaml'"
        ])
    ])
    environment_config=PathJoinSubstitution([
        package_share,
        "config",
        "environments",
        PythonExpression([
            "'",
            environment,
            "' + '.yaml'"
        ])
    ])  
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot',
            default_value='go2',
        ),
        DeclareLaunchArgument(
            'environment',
            default_value='indoor'
        ),
        Node(
            package='motion_safety_stack',
            executable='robot_info',
            name='robot_info',
            parameters=[
                robot_config,
                environment_config
            ]
        ),
                Node(
            package='motion_safety_stack',
            executable='velocity_source',
            name='velocity_source',
            parameters=[
                robot_config,
                environment_config
            ]
        ),
        Node(
            package='motion_safety_stack',
            executable='velocity_limiter',
            name='velocity_limiter',
            parameters=[
                robot_config,
                environment_config
            ]
        ),
        Node(
            package='motion_safety_stack',
            executable='velocity_monitor',
            name='velocity_monitor'
        )

    ])