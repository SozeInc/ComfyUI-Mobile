# Comfy Mobile
# by Soze Inc - 2024-05 
# https://github.com/SozeInc/ComfyUI-SozeNodes
import os
import requests


import comfy.samplers

import customdataclasses



# Get the absolute path of various directories
mobilenodes_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
custom_nodes_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..', '..'))









########################################################################################################################
# Comfy_Mobile_Settings_Launcher
class Settings_Launcher:
    @classmethod
    def INPUT_TYPES(cls):
        custom_max = 25
        inputs = {
            "required": {
                "resume": (["Always Resume", "Wait to Resume", "Resume Once"], {"default": "Resume Once"})
            },
            "optional": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                "width": ("INT", {"default": 512, "min": 1, "max": 8192}),
                "height": ("INT", {"default": 512, "min": 1, "max": 8192}),
                "batch_count": ("INT", {"default": 1, "min": 1, "max": 1024}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                "denoise": ("float", {"default": 1.0, "min": 0.0, "max": 1.0}),

                "custom_value_count": ("INT", {"default": 0, "min": 1, "max": custom_max, "step": 1, "hideInput": True}),

                "custom_name_1": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_1": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_1": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_2": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_2": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_2": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_3": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_3": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_3": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_4": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_4": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_4": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_5": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_5": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_5": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_6": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_6": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_6": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_7": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_7": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_7": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_8": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_8": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_8": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_9": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_9": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_9": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_10": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_10": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_10": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_11": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_11": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_11": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_12": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_12": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_12": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_13": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_13": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_13": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_14": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_14": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_14": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_15": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_15": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_15": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_16": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_16": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_16": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_17": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_17": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_17": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_18": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_18": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_18": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_19": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_19": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_19": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_20": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_20": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_20": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_21": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_21": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_21": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_22": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_22": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_22": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_23": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_23": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_23": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_24": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_24": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_24": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),

                "custom_name_25": ("STRING", {"default": ""}, {"hideInput": True}),
                "custom_type_25": (["STRING", "INT", "FLOAT", "BOOLEAN"], {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                "custom_value_25": ("STRING", {"default": ""}, {"forceInput": True}, {"hideInput": True}),
                
            }
        }

        return inputs

    RETURN_TYPES = (customdataclasses.SettingsLauncherData)
    RETURN_NAMES = ("settings_launcher_outputs")
    FUNCTION = "settings_launcher"
    CATEGORY = "Comfy Mobile"

    def settings_launcher(self, seed,steps,cfg,width,height,batch_count,sampler_name,scheduler,denoise,custom_name_1, custom_type_1, custom_value_1, custom_name_2, custom_type_2, custom_value_2, custom_name_3, custom_type_3, custom_value_3, custom_name_4, custom_type_4, custom_value_4, custom_name_5, custom_type_5, custom_value_5, custom_name_6, custom_type_6, custom_value_6, custom_name_7, custom_type_7, custom_value_7, custom_name_8, custom_type_8, custom_value_8, custom_name_9, custom_type_9, custom_value_9, custom_name_10, custom_type_10, custom_value_10, custom_name_11, custom_type_11, custom_value_11, custom_name_12, custom_type_12, custom_value_12, custom_name_13, custom_type_13, custom_value_13, custom_name_14, custom_type_14, custom_value_14,  custom_name_15, custom_type_15, custom_value_15, custom_name_16, custom_type_16, custom_value_16, custom_name_17, custom_type_17, custom_value_17, custom_name_18, custom_type_18, custom_value_18, custom_name_19, custom_type_19, custom_value_19, custom_name_20, custom_type_20, custom_value_20, custom_name_21, custom_type_21, custom_value_21, custom_name_22, custom_type_22, custom_value_22, custom_name_23, custom_type_23, custom_value_23, custom_name_24, custom_type_24, custom_value_24, custom_name_25, custom_type_25, custom_value_25):
        
        output = customdataclasses.SettingsLauncherData(seed, steps, cfg, width, height, batch_count, sampler_name, scheduler, denoise, 
                      custom_name_1, custom_type_1, custom_value_1, custom_name_2, custom_type_2, custom_value_2, 
                      custom_name_3, custom_type_3, custom_value_3, custom_name_4, custom_type_4, custom_value_4, 
                      custom_name_5, custom_type_5, custom_value_5, custom_name_6, custom_type_6, custom_value_6, 
                      custom_name_7, custom_type_7, custom_value_7, custom_name_8, custom_type_8, custom_value_8, 
                      custom_name_9, custom_type_9, custom_value_9, custom_name_10, custom_type_10, custom_value_10, 
                      custom_name_11, custom_type_11, custom_value_11, custom_name_12, custom_type_12, custom_value_12, 
                      custom_name_13, custom_type_13, custom_value_13, custom_name_14, custom_type_14, custom_value_14, 
                      custom_name_15, custom_type_15, custom_value_15, custom_name_16, custom_type_16, custom_value_16, 
                      custom_name_17, custom_type_17, custom_value_17, custom_name_18, custom_type_18, custom_value_18, 
                      custom_name_19, custom_type_19, custom_value_19, custom_name_20, custom_type_20, custom_value_20, 
                      custom_name_21, custom_type_21, custom_value_21, custom_name_22, custom_type_22, custom_value_22, 
                      custom_name_23, custom_type_23, custom_value_23, custom_name_24, custom_type_24, custom_value_24, 
                      custom_name_25, custom_type_25, custom_value_25)

        
        return (output)



    def get_settings():

        # Replace with your actual API endpoint
        url = "http://localhost:49163/GetSettings"

        # Replace with your actual file path
        file_path = os.path.join(mobilenodes_dir, "token.txt")

        # Open the file and read its contents
        with open(file_path, "r") as file:
            user_token = file.read()

        # Make the GET request
        response = requests.get(url, params={"userToken": user_token})

        # Check the response
        if response.status_code == 200:
            # If the request was successful, print the settings
            print(response.json())
        else:
            # If the request failed, print the status code
            print(f"Request failed with status code {response.status_code}")








########################################################################################################################
# Comfy_Mobile_Settings_Launcher_Outputs
class Settings_Launcher_Outputs:
    @classmethod
    def INPUT_TYPES(cls):
        custom_max = 25
        inputs = {
            "required": {
                "settings_launcher_outputs": (customdataclasses.SettingsLauncherData, {"default": ""})
            }
        }
        return inputs

    RETURN_TYPES = ("INT","INT","FLOAT","INT","INT","INT",comfy.samplers.KSampler.SAMPLERS,comfy.samplers.KSampler.SCHEDULERS,"FLOAT","INT","STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("seed","steps","cfg","width","height","batch_count","sampler_name","scheduler","denoise","custom_name_1", "custom_type_1", "custom_value_1", "custom_name_2", "custom_type_2", "custom_value_2", "custom_name_3", "custom_type_3", "custom_value_3", "custom_name_4", "custom_type_4", "custom_value_4", "custom_name_5", "custom_type_5", "custom_value_5", "custom_name_6", "custom_type_6", "custom_value_6", "custom_name_7", "custom_type_7", "custom_value_7", "custom_name_8", "custom_type_8", "custom_value_8", "custom_name_9", "custom_type_9", "custom_value_9", "custom_name_10", "custom_type_10", "custom_value_10", "custom_name_11", "custom_type_11", "custom_value_11", "custom_name_12", "custom_type_12", "custom_value_12", "custom_name_13", "custom_type_13", "custom_value_13", "custom_name_14", "custom_type_14", "custom_value_14",  "custom_name_15", "custom_type_15", "custom_value_15", "custom_name_16", "custom_type_16", "custom_value_16", "custom_name_17", "custom_type_17", "custom_value_17", "custom_name_18", "custom_type_18", "custom_value_18", "custom_name_19", "custom_type_19", "custom_value_19", "custom_name_20", "custom_type_20", "custom_value_20", "custom_name_21", "custom_type_21", "custom_value_21", "custom_name_22", "custom_type_22", "custom_value_22", "custom_name_23", "custom_type_23", "custom_value_23", "custom_name_24", "custom_type_24", "custom_value_24", "custom_name_25", "custom_type_25", "custom_value_25")
    FUNCTION = "SendSettingsLauncherOutputs"
    CATEGORY = "Comfy Mobile"

def SendSettingsLauncherOutputs(settings_launcher_outputs):
    return (settings_launcher_outputs.seed,settings_launcher_outputs.steps,settings_launcher_outputs.cfg,settings_launcher_outputs.width,settings_launcher_outputs.height,settings_launcher_outputs.batch_count,settings_launcher_outputs.sampler_name,settings_launcher_outputs.scheduler,settings_launcher_outputs.denoise,settings_launcher_outputs.custom_name_1,settings_launcher_outputs.custom_type_1,settings_launcher_outputs.custom_value_1,settings_launcher_outputs.custom_name_2,settings_launcher_outputs.custom_type_2,settings_launcher_outputs.custom_value_2,settings_launcher_outputs.custom_name_3,settings_launcher_outputs.custom_type_3,settings_launcher_outputs.custom_value_3,settings_launcher_outputs.custom_name_4,settings_launcher_outputs.custom_type_4,settings_launcher_outputs.custom_value_4,settings_launcher_outputs.custom_name_5,settings_launcher_outputs.custom_type_5,settings_launcher_outputs.custom_value_5,settings_launcher_outputs.custom_name_6,settings_launcher_outputs.custom_type_6,settings_launcher_outputs.custom_value_6,settings_launcher_outputs.custom_name_7,settings_launcher_outputs.custom_type_7,settings_launcher_outputs.custom_value_7,settings_launcher_outputs.custom_name_8,settings_launcher_outputs.custom_type_8,settings_launcher_outputs.custom_value_8,settings_launcher_outputs.custom_name_9,settings_launcher_outputs.custom_type_9,settings_launcher_outputs.custom_value_9,settings_launcher_outputs.custom_name_10,settings_launcher_outputs.custom_type_10,settings_launcher_outputs.custom_value_10,settings_launcher_outputs.custom_name_11,settings_launcher_outputs.custom_type_11,settings_launcher_outputs.custom_value_11,settings_launcher_outputs.custom_name_12,settings_launcher_outputs.custom_type_12,settings_launcher_outputs.custom_value_12,settings_launcher_outputs.custom_name_13,settings_launcher_outputs.custom_type_13,settings_launcher_outputs.custom_value_13,settings_launcher_outputs.custom_name_14,settings_launcher_outputs.custom_type_14,settings_launcher_outputs.custom_value_14,settings_launcher_outputs.custom_name_15,settings_launcher_outputs.custom_type_15,settings_launcher_outputs.custom_value_15,settings_launcher_outputs.custom_name_16,settings_launcher_outputs.custom_type_16,settings_launcher_outputs.custom_value_16,settings_launcher_outputs.custom_name_17,settings_launcher_outputs.custom_type_17,settings_launcher_outputs.custom_value_17,settings_launcher_outputs.custom_name_18,settings_launcher_outputs.custom_type_18,settings_launcher_outputs.custom_value_18,settings_launcher_outputs.custom_name_19,settings_launcher_outputs.custom_type_19,settings_launcher_outputs.custom_value_19,settings_launcher_outputs.custom_name_20,settings_launcher_outputs.custom_type_20,settings_launcher_outputs.custom_value_20,settings_launcher_outputs.custom_name_21,settings_launcher_outputs.custom_type_21,settings_launcher_outputs.custom_value_21,settings_launcher_outputs.custom_name_22,settings_launcher_outputs.custom_type_22,settings_launcher_outputs.custom_value_22,settings_launcher_outputs.custom_name_23,settings_launcher_outputs.custom_type_23,settings_launcher_outputs.custom_value_23,settings_launcher_outputs.custom_name_24,settings_launcher_outputs.custom_type_24,settings_launcher_outputs.custom_value_24,settings_launcher_outputs.custom_name_25,settings_launcher_outputs.custom_type_25,settings_launcher_outputs.custom_value_25)