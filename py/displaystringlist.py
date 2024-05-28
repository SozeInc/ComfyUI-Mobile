# ComfyUI Mobile Nodes - A collection of ComfyUI Mobile related custom nodes.
# by Soze Inc - 2024-05 
# https://github.com/SozeInc/ComfyUI-Mobile

import json
#from .constants import get_category, get_name


class Display_Strings_List:
  """Display any data node."""

  NAME = "Display Strings List"
  CATEGORY = "Comfy Mobile"

  @classmethod
  def INPUT_TYPES(cls):  # pylint: disable = invalid-name, missing-function-docstring
    return {
      "required": {
        "source": (any, {}),
      },
    }

  RETURN_TYPES = ()
  FUNCTION = "main"
  OUTPUT_NODE = True

  def main(self, source=None):
    value = 'None'
    if source is not None:
      try:
        value = json.dumps(source)
      except Exception:
        try:
          value = str(source)
        except Exception:
          value = 'source exists, but could not be serialized.'

    return {"ui": {"text": (value,)}}


