import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable, TimerAction  # 新增 TimerAction

def generate_launch_description():
    return LaunchDescription([
        # 第 1 组：立即启动
        Node(
            package='voice_chat_py',
            executable='voice_chat_node',
            name='voice_chat_node',
            output='screen'
        ),

        ExecuteProcess(
            cmd=[
                "x-terminal-emulator",
                "--new-process",
                "-e",
                'bash',
                '-c', 
                'source ~/.bashrc && '
                'ros2 run joy joy_node & '
                'ros2 run sport_control sport_control_node --ros-args -p network_interface:=enx00e04c8d0eff;'
                'read -p "Press enter to close"'
            ],
            output="screen",
        ),

        TimerAction(
            period=1.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        "x-terminal-emulator",
                        "--new-process",
                        "-e",
                        'bash',
                        '-c',
                        'source ~/.bashrc && '
                        'rviz2 -d /home/smx/unitree_ros2_250221/Ros2Go2Estimator/other/SMXFE_odm.rviz; '
                        'read -p "Press enter to close"'
                    ],
                    output='screen',
                )
            ]
        ),

        # 第 2 组：延迟 3 秒启动
        TimerAction(
            period=3.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        "x-terminal-emulator",
                        "--new-process",
                        "-e",
                        'bash',
                        '-c',
                        'source ~/.bashrc && '
                        'ros2 run fusion_estimator fusion_estimator_node --ros-args -p network_interface:=enx00e04c8d0eff & '
                        'ros2 run message_handle message_handle_node;'
                        'read -p "Press enter to close"'
                    ],
                    output="screen",
                ),
            ]
        ),

        # 第 3 组：延迟 6 秒启动（即第 2 组启动后 3 秒）
        TimerAction(
            period=5.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        "x-terminal-emulator",
                        "--new-process",
                        "-e",
                        'bash',
                        '-c',
                        'source ~/.bashrc && '
                        'ros2 run slam_toolbox async_slam_toolbox_node --ros-args --params-file /home/smx/unitree_ros2_250221/Ros2Go2Estimator/other/slam_params.yaml&'
                        # 'ros2 launch nav2_bringup bringup_launch.py \
                        #     map:=/home/smx/unitree_ros2_250221/Ros2Go2Estimator/local_file/map_new.yaml \
                        #     params_file:=/home/smx/unitree_ros2_250221/Ros2Go2Estimator/other/Guide.yaml; '
                        'read -p "Press enter to close"'
                    ],
                    output='screen',
                )
            ]
        ),
    ]

    # rviz2 -d /home/smx/unitree_ros2_250221/Ros2Go2Estimator/other/SMXFE_odm.rviz
    # ros2 run rqt_tf_tree rqt_tf_tree
)

