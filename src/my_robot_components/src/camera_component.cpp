#include "my_robot_components/camera_component.hpp"

#include <chrono>
#include <functional>

#include "rclcpp_components/register_node_macro.hpp"
namespace my_robot_components
{
CameraComponent::CameraComponent(
    const rclcpp::NodeOptions& options
)
: Node(
    "camera_component",
    options
)
{
    publisher_ =
        this->create_publisher<std_msgs::msg::String>(
            "camera_data",
            10
        );
    RCLCPP_INFO(
        this->get_logger(),
        "Camera component loaded"
    );
    timer_ =
        this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(
                &CameraComponent::timer_callback,
                this
            )
        );
}
void CameraComponent::timer_callback()
{
    std_msgs::msg::String msg;
    msg.data = "Camera component publishing";
    publisher_->publish(
        msg
    );
    RCLCPP_INFO(
        this->get_logger(),
        "%s",
        msg.data.c_str()
        );
    

}

} // namespace my_robot_components
RCLCPP_COMPONENTS_REGISTER_NODE(
    my_robot_components::CameraComponent
)
