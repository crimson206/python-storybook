from utils import set_indent
from typing import Dict
from ..core import StoryHub, Story, StoryMeta
from auto_docs_templates import story_docs_template_base
import json


class AutoDocsAPI:
    def __init__(self):
        pass

    def _generate_autodocs_base(self, story: Story, story_meta: StoryMeta) -> Dict:
        story_meta = story_meta.model_dump()
        story_meta["type_hints"] = json.dumps(story_meta["type_hints"], indent=2)
        story_meta["result"] = story.render()
        return story_meta

    def _set_indent(self, story_meta: Dict) -> Dict:
        indent_targets = [
            "render_name",
            "docs",
            "type_hints",
            "result",
        ]

        for key, value in story_meta.items():
            if key in indent_targets:
                story_meta[key] = set_indent(value)

    def _generate_auto_docs(self, story_meta: Dict) -> str:

        formatted = story_docs_template_base.format(**story_meta)

        return formatted

    def generate_auto_docs(self, story: Story) -> str:
        story_meta = StoryHub.get_story_meta(story)
        story_meta = self._generate_autodocs_base(story, story_meta)
        auto_docs = self._set_indent(story_meta)
        return auto_docs
