import json
#from .constants import get_category, get_name


sozenodes_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
custom_nodes_dir = os.path.abspath(os.path.join(sozenodes_dir, '..'))
comfy_dir = os.path.abspath(os.path.join(sozenodes_dir, '..', '..'))


class Soze_Display_Strings_List:
  """Display any data node."""

  NAME = "Soze Display Strings List"
  CATEGORY = "Soze Nodes"

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

