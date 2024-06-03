from ..core import StoryMeta
import json

def set_indent(text: str, indent: int = 4):
    space = " " * indent
    split = text.split('\n')
    split = [space + line for line in split]
    return "\n".join(split)
