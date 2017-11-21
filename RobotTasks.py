from enum import Enum

class RobotTasksEnum(Enum):
    SCISSOR = "scissor"
    FORCEP = "forcep"
    NEEDLE = "needle holder"
    TEST = "test"

robot_tasks_list = [e.value for e in RobotTasksEnum]

