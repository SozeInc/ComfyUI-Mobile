# ComfyUI Mobile Nodes - A collection of ComfyUI Mobile related custom nodes.
# by Soze Inc - 2024-05 
# https://github.com/SozeInc/ComfyUI-Mobile


import os
import subprocess
import importlib.util
import shutil
import sys
import traceback

from .py.ultimateconcat import Ultimate_Concat
from .py.sendnotification import Send_Notification
from .py.settingslauncher import Settings_Launcher#, Settings_Launcher_Outputs

NODE_CLASS_MAPPINGS = { "Ultimate Concat (Mobile)": Ultimate_Concat,
                        "Send Notification (Mobile)": Send_Notification,
                        "Settings Launcher (Mobile)": Settings_Launcher,
                        #"Mobile_Settings_Launcher_Data": Settings_Launcher_Outputs
                        }

NODE_DISPLAY_NAME_MAPPINGS = { "Ultimate_Concat": "Ultimate Concat (Mobile)",
                              "Send_Notification": "Send Notification (Mobile)",
                              "Settings_Launcher": "Settings Launcher (Mobile)",
                              #"Settings_Launcher_Data": "Settings Launcher Outputs (Mobile)"
                              }

WEB_DIRECTORY = "js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']