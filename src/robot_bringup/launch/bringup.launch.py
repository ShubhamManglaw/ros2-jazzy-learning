from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch.actions import LogInfo
import os


def generate_launch_description():

    bringup_dir = get_package_share_directory(
        'robot_bringup'
    )
    simulation_arg = DeclareLaunchArgument(
        "simulation",
        default_value="false",
        description="Simulation mode"
    )
    robot_namespace_arg = DeclareLaunchArgument(
        "robot_namespace",
        default_value="robot1",
        description="Robot namespace"
    )

    robot_namespace = LaunchConfiguration(
        "robot_namespace"
    )

    simulation = LaunchConfiguration("simulation")

    management_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_dir,
                'launch',
                'management.launch.py'
            )
        )
    )

    telemetry_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_dir,
                'launch',
                'telemetry.launch.py'
            )
        ),condition=IfCondition(simulation)
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_dir,
                'launch',
                'navigation.launch.py'
            )
        )
    )
    return LaunchDescription([
        simulation_arg,
        robot_namespace_arg,
        management_launch,
        telemetry_launch,
        navigation_launch
    ])