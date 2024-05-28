import os
import subprocess
import importlib.util
import shutil
import sys
import traceback

from .py.ultimateconcat import Soze_Ultimate_Concat
from .py.sendnotification import Soze_Send_Notification

NODE_CLASS_MAPPINGS = { "Soze_Ultimate_Concat": Soze_Ultimate_Concat,
                        "Soze_Send_Notification": Soze_Send_Notification}

NODE_DISPLAY_NAME_MAPPINGS = { "Soze_Ultimate_Concat": "Soze Ultimate Concat",
                              "Soze_Send_Notification": "Soze Send Notification"}

WEB_DIRECTORY = "js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']