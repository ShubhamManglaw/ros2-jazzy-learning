from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command , PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import FindExecutable

def generate_launch_description():
    pkg_path = FindPackageShare("my_robot_description")
    xacro_file = PathJoinSubstitution([pkg_path, "urdf", "robot.urdf.xacro"])
    rviz_config = PathJoinSubstitution([pkg_path,"rviz","display.rviz"])
    robot_description = ParameterValue(
        Command([
            FindExecutable(name="xacro"),
            " ",
            xacro_file,
        ]),
        value_type=str,
        
    )
    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": robot_description
            }],
            output="screen"
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="screen"
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen"
        )
    ])