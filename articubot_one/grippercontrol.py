#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class JointTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('joint_trajectory_publisher')
        self.publisher = self.create_publisher(JointTrajectory, '/set_joint_trajectory', 10)

    def publish_joint_trajectory(self):
        joint_trajectory_msg = JointTrajectory()
        joint_trajectory_msg.joint_names = ['arm_joint']  # Replace with your joint name

        joint_trajectory_point = JointTrajectoryPoint()
        joint_trajectory_point.positions = [1]  # Replace with your desired position
        joint_trajectory_msg.points.append(joint_trajectory_point)

        self.publisher.publish(joint_trajectory_msg)
        self.get_logger().info('Joint trajectory point published')

def main(args=None):
    rclpy.init(args=args)

    joint_trajectory_publisher = JointTrajectoryPublisher()
    print("Trying")
    try:
        joint_trajectory_publisher.publish_joint_trajectory()
        rclpy.spin_once(joint_trajectory_publisher, timeout_sec=1)
        print("YES")
    except KeyboardInterrupt:
        pass
