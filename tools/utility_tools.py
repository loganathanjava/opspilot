from datetime import datetime

from google.adk.tools import FunctionTool


def get_current_time() -> str:
    """
    Returns the current local time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


current_time_tool = FunctionTool(get_current_time)