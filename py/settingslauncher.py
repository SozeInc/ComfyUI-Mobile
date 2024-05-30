# ComfyUI Mobile Nodes - A collection of ComfyUI Mobile related custom nodes.
# by Soze Inc - 2024-05 
# https://github.com/SozeInc/ComfyUI-Mobile
import os
import requests
import comfy.samplers

from server import PromptServer
from comfy.model_management import InterruptProcessingException

#from .settingslauncherserver import MessageHolder, Cancelled
from settingslauncherflowcontrol import FlowControl, Cancelled
import random

# Get the absolute path of various directories
mobilenodes_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
custom_nodes_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(mobilenodes_dir, '..', '..'))



class SettingsLauncherData:
    def __init__(self, seed, steps, cfg, width, height, batch_count, sampler_name, scheduler, denoise):
        self.seed = seed
        self.steps = steps
        self.cfg = cfg
        self.width = width
        self.height = height
        self.batch_count = batch_count
        self.sampler_name = sampler_name
        self.scheduler = scheduler
        self.denoise = denoise


    def to_dict(self):
        return self.__dict__






########################################################################################################################
# Comfy_Mobile_Settings_Launcher
class Settings_Launcher:
    # RETURN_NAMES = (SettingsLauncherData)
    # RETURN_TYPES = ('Settings_Launcher_Outputs')
    RETURN_TYPES = ("INT","INT","FLOAT","INT","INT","INT",comfy.samplers.KSampler.SAMPLERS,comfy.samplers.KSampler.SCHEDULERS,"FLOAT")
    RETURN_NAMES = ("seed","steps","cfg","width","height","batch_count","sampler_name","scheduler","denoise")

    FUNCTION = "settings_launcher"
    CATEGORY = "Comfy Mobile"
    INPUT_IS_LIST=False
    OUTPUT_NODE = False
    last_ic = {}    
    @classmethod
    def INPUT_TYPES(cls):
        custom_max = 25
        inputs = {
            "required": {
                "resume": (["Always Proceed", "Wait to Proceed", "Proceed Once"], {"default": "Proceed Once"}),
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
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0})
            },
        }
        return inputs

    @classmethod
    def IS_CHANGED(cls, resume, id, **kwargs):
        if (resume!="Wait to Proceed" or not id[0] in cls.last_ic): cls.last_ic[id[0]] = random.random()
        return cls.last_ic[id[0]]


    def settings_launcher(self,resume,seed,steps,cfg,width,height,batch_count,sampler_name,scheduler,denoise):
        FlowControl.start()
        #Get Settings Here

        # wait for user confirmation
        try:
            if (resume == "Wait to Proceed"):
                print("[ComfyMobile] Wait to proceed")
                FlowControl.waitToProceed()
            # is_block_condition = (resume == "Wait to Proceed")
            # is_blocking_mode = (resume not in ["Always Proceed", "Proceed Once"])
            # print("[ComfyMobile] Wait For Message ID: " + id)
            # MessageHolder.waitForMessage(id) if (is_blocking_mode and is_block_condition) else [0]
        except Cancelled:
            print("[ComfyMobile] InterruptProcessingException")
            raise InterruptProcessingException()

        #if (resume == "Proceed Once"): resume = "Wait to Proceed"
        
        settings_launcher_outputs = SettingsLauncherData(seed, steps, cfg, width, height, batch_count, sampler_name, scheduler, denoise)
        
        print("[ComfyMobile] Return Settings")
        return (settings_launcher_outputs.seed,settings_launcher_outputs.steps,settings_launcher_outputs.cfg,settings_launcher_outputs.width,settings_launcher_outputs.height,
                settings_launcher_outputs.batch_count,settings_launcher_outputs.sampler_name,settings_launcher_outputs.scheduler,settings_launcher_outputs.denoise)








########################################################################################################################
# Comfy_Mobile_Settings_Launcher_Outputs
# class Settings_Launcher_Outputs:
#     @classmethod
#     def INPUT_TYPES(cls):
#         custom_max = 25
#         inputs = {
#             "required": {
#                 "settings_launcher_outputs": (SettingsLauncherData, {"default": ""})
#             }
#         }
#         return inputs

#     RETURN_TYPES = ("INT","INT","FLOAT","INT","INT","INT",comfy.samplers.KSampler.SAMPLERS,comfy.samplers.KSampler.SCHEDULERS,"FLOAT","INT","STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
#     RETURN_NAMES = ("seed","steps","cfg","width","height","batch_count","sampler_name","scheduler","denoise","custom_value_count","custom_name_1", "custom_type_1", "custom_value_1", "custom_name_2", "custom_type_2", "custom_value_2", "custom_name_3", "custom_type_3", "custom_value_3", "custom_name_4", "custom_type_4", "custom_value_4", "custom_name_5", "custom_type_5", "custom_value_5", "custom_name_6", "custom_type_6", "custom_value_6", "custom_name_7", "custom_type_7", "custom_value_7", "custom_name_8", "custom_type_8", "custom_value_8", "custom_name_9", "custom_type_9", "custom_value_9", "custom_name_10", "custom_type_10", "custom_value_10", "custom_name_11", "custom_type_11", "custom_value_11", "custom_name_12", "custom_type_12", "custom_value_12", "custom_name_13", "custom_type_13", "custom_value_13", "custom_name_14", "custom_type_14", "custom_value_14",  "custom_name_15", "custom_type_15", "custom_value_15", "custom_name_16", "custom_type_16", "custom_value_16", "custom_name_17", "custom_type_17", "custom_value_17", "custom_name_18", "custom_type_18", "custom_value_18", "custom_name_19", "custom_type_19", "custom_value_19", "custom_name_20", "custom_type_20", "custom_value_20", "custom_name_21", "custom_type_21", "custom_value_21", "custom_name_22", "custom_type_22", "custom_value_22", "custom_name_23", "custom_type_23", "custom_value_23", "custom_name_24", "custom_type_24", "custom_value_24", "custom_name_25", "custom_type_25", "custom_value_25")
#     FUNCTION = "SendSettingsLauncherOutputs"
#     CATEGORY = "Comfy Mobile"

# def SendSettingsLauncherOutputs(settings_launcher_outputs):
#     return (settings_launcher_outputs.seed,settings_launcher_outputs.steps,settings_launcher_outputs.cfg,settings_launcher_outputs.width,settings_launcher_outputs.height,settings_launcher_outputs.batch_count,settings_launcher_outputs.sampler_name,settings_launcher_outputs.scheduler,settings_launcher_outputs.denoise,settings_launcher_outputs.custom_name_1,settings_launcher_outputs.custom_type_1,settings_launcher_outputs.custom_value_1,settings_launcher_outputs.custom_name_2,settings_launcher_outputs.custom_type_2,settings_launcher_outputs.custom_value_2,settings_launcher_outputs.custom_name_3,settings_launcher_outputs.custom_type_3,settings_launcher_outputs.custom_value_3,settings_launcher_outputs.custom_name_4,settings_launcher_outputs.custom_type_4,settings_launcher_outputs.custom_value_4,settings_launcher_outputs.custom_name_5,settings_launcher_outputs.custom_type_5,settings_launcher_outputs.custom_value_5,settings_launcher_outputs.custom_name_6,settings_launcher_outputs.custom_type_6,settings_launcher_outputs.custom_value_6,settings_launcher_outputs.custom_name_7,settings_launcher_outputs.custom_type_7,settings_launcher_outputs.custom_value_7,settings_launcher_outputs.custom_name_8,settings_launcher_outputs.custom_type_8,settings_launcher_outputs.custom_value_8,settings_launcher_outputs.custom_name_9,settings_launcher_outputs.custom_type_9,settings_launcher_outputs.custom_value_9,settings_launcher_outputs.custom_name_10,settings_launcher_outputs.custom_type_10,settings_launcher_outputs.custom_value_10,settings_launcher_outputs.custom_name_11,settings_launcher_outputs.custom_type_11,settings_launcher_outputs.custom_value_11,settings_launcher_outputs.custom_name_12,settings_launcher_outputs.custom_type_12,settings_launcher_outputs.custom_value_12,settings_launcher_outputs.custom_name_13,settings_launcher_outputs.custom_type_13,settings_launcher_outputs.custom_value_13,settings_launcher_outputs.custom_name_14,settings_launcher_outputs.custom_type_14,settings_launcher_outputs.custom_value_14,settings_launcher_outputs.custom_name_15,settings_launcher_outputs.custom_type_15,settings_launcher_outputs.custom_value_15,settings_launcher_outputs.custom_name_16,settings_launcher_outputs.custom_type_16,settings_launcher_outputs.custom_value_16,settings_launcher_outputs.custom_name_17,settings_launcher_outputs.custom_type_17,settings_launcher_outputs.custom_value_17,settings_launcher_outputs.custom_name_18,settings_launcher_outputs.custom_type_18,settings_launcher_outputs.custom_value_18,settings_launcher_outputs.custom_name_19,settings_launcher_outputs.custom_type_19,settings_launcher_outputs.custom_value_19,settings_launcher_outputs.custom_name_20,settings_launcher_outputs.custom_type_20,settings_launcher_outputs.custom_value_20,settings_launcher_outputs.custom_name_21,settings_launcher_outputs.custom_type_21,settings_launcher_outputs.custom_value_21,settings_launcher_outputs.custom_name_22,settings_launcher_outputs.custom_type_22,settings_launcher_outputs.custom_value_22,settings_launcher_outputs.custom_name_23,settings_launcher_outputs.custom_type_23,settings_launcher_outputs.custom_value_23,settings_launcher_outputs.custom_name_24,settings_launcher_outputs.custom_type_24,settings_launcher_outputs.custom_value_24,settings_launcher_outputs.custom_name_25,settings_launcher_outputs.custom_type_25,settings_launcher_outputs.custom_value_25)