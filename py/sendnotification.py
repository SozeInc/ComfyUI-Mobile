# Mobile Nodes - A collection of ComfyUI notification related custom nodes.
# by Soze Inc - 2024-05 
# https://github.com/SozeInc/ComfyUI-SozeNodes
import os
import subprocess

# Get the absolute path of various directories
mobilenodes_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
custom_nodes_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..', '..'))


########################################################################################################################
# Soze_Send_Notification
class Soze_Send_Notification:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "message": ("STRING", {"default": ""}),
                "send_media": ("BOOLEAN", {"default": False})
            },
            "optional": {
                "messagePrefix": ("STRING", {"default": ""}),
                "messageSuffix": ("STRING", {"default": ""})
            }
        }

        return inputs

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output", "error")
    FUNCTION = "send_notification"
    CATEGORY = "Soze Nodes"

    def send_notification(self, message, messagePrefix, messageSuffix):
        notifier = mobilenodes_dir + "\\notifier\\sozenotifier.exe "
        print("SOZE: Notifier: " + notifier)
        process = subprocess.Popen([notifier, messagePrefix + message + messageSuffix], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        return (stdout.decode(),stderr.decode())