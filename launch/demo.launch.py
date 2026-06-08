from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg = get_package_share_directory("automail_moveit_config")

    moveit_config = (
        MoveItConfigsBuilder("automail", package_name="automail_moveit_config")
        .robot_description(
            file_path=os.path.join(pkg, "config", "automail.urdf.xacro")
        )
        .robot_description_semantic(
            file_path=os.path.join(pkg, "config", "automail.srdf")
        )
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)