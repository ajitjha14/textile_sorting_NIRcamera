#!/usr/bin/env python3

# Copyright 2024 Trossen Robotics
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import numpy as np
from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

"""
This script makes the end-effector perform pick, pour, and place tasks.
Note that this script may not work for every arm as it was designed for the wx250.
Make sure to adjust commanded joint positions and poses as necessary.

To get started, open a terminal and type:

    ros2 launch interbotix_xsarm_control xsarm_control.launch.py robot_model:=wx250

Then change to this directory and type:

    python3 bartender.py
"""

# Define the function to set end-effector pose and joint position
def detecting_home_position(bot):
    # Command to set end-effector pose components
    bot.arm.set_ee_pose_components(x=0.3, z=0.55)
    #bot.arm.set_ee_pose_components(x=0.2, z=0.5)
    
    # Command to set the wrist joint position
    bot.arm.set_single_joint_position(joint_name='wrist_angle', position=np.pi / 1.5)
    #bot.arm.set_single_joint_position(joint_name='upper_arm_angle', position=np.pi / 1.7)

def main():
    # Initialize the robot object
    bot = InterbotixManipulatorXS(
        robot_model='wx250s',
        group_name='arm',
        gripper_name='gripper',
    )

    robot_startup()  # Start the robot system

    if bot.arm.group_info.num_joints < 5:
        bot.get_node().logfatal('This demo requires the robot to have at least 5 joints!')
        robot_shutdown()
        sys.exit()
       

    # Move the robot using the function
    #bot.arm.go_to_sleep_pose()
    detecting_home_position(bot)

    # Additional movement and gripper commands (commented out for now)
    # bot.gripper.release()
    # bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
    # bot.gripper.grasp()
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    # bot.arm.set_single_joint_position(joint_name='waist', position=-np.pi/2.0)
    # bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    # bot.arm.set_single_joint_position(joint_name='waist', position=np.pi/2.0)
    # bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
    # bot.gripper.release()
    # bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    # bot.arm.go_to_home_pose()
    #bot.arm.set_ee_pose_components(x=0.37, y= 0.16, z=0.08) #   X=0.37, Y=0.16, Z=0.05
    #bot.arm.go_to_sleep_pose()  # Send the robot arm to its sleep pose
    #bot.arm.set_ee_pose_components(x=0.15, z=0.21)
    #bot.arm.set_ee_pose_components(x=  0.53   +0.01, y = 0.096   , z=0.1)

    robot_shutdown()  # Shutdown the robot system


if __name__ == '__main__':
    main()

