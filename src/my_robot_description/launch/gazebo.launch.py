from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command , PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import FindExecutable
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction

def generate_launch_description():
    pkg_path = FindPackageShare("my_robot_description")
    xacro_file = PathJoinSubstitution([pkg_path, "urdf", "robot.urdf.xacro"])
    rviz_config = PathJoinSubstitution([pkg_path,"rviz","display.rviz"])
    world_file = PathJoinSubstitution([pkg_path, "worlds", "empty_lidar.sdf"])
    robot_description = ParameterValue(
        Command([
            FindExecutable(name="xacro"),
            " ",
            xacro_file,
        ]),
        value_type=str,
        
    )
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            ])
        ),
        launch_arguments={
            "gz_args": [world_file]
        }.items()
    )
    return LaunchDescription([
        gazebo,
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": robot_description,
                "use_sim_time": True,
            }],
            output="screen"
        ),
        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
                "/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry",
                "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
                "/model/my_robot/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V",
                "/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
            ],
            remappings=[("/model/my_robot/tf", "/tf")],
            output="screen",
        ),
        TimerAction(
            period=5.0,
            actions=[
                Node(
                    package="ros_gz_sim",
                    executable="create",
                    arguments=[
                        "-world", "empty",
                        "-topic", "/robot_description",
                        "-name", "my_robot",
                        "-z", "0.5"
                    ],
                    output="screen",
                )
            ]
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen",
            parameters=[{
                "use_sim_time": True
            }]
        )
    ])