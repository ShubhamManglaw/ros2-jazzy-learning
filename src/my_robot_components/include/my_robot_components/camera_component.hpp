#pragma once
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
namespace my_robot_components
{

class CameraComponent : public rclcpp::Node
{
public:
    explicit CameraComponent(
        const rclcpp::NodeOptions & options
    );
private:
    void timer_callback();
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

};

}