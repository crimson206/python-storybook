from pydantic import BaseModel
from .utils import set_indent
from typing import Dict, List
from python_storybook.core import StoryHub, Story, StoryMeta


class AutoDocs(BaseModel):
    title: str
    story_metas: List[StoryMeta]


class AutoDocsAPI:
    @staticmethod
    def generate_auto_docs(title: str,) -> AutoDocs:
        story_manager = StoryHub.get_manager(title)
        stories = story_manager.get_stories()
        autodocs = f"# {title}\n\n"
        autodocs = []
        for story in stories:
            autodocs.append(AutoDocsAPI.generate_auto_doc(story))

        autodocs = AutoDocs(
            title=title,
            story_metas=autodocs
        )

        return autodocs

    @staticmethod
    def generate_auto_doc(story_or_path: Story | str) -> StoryMeta:
        if isinstance(story_or_path, Story):
            story = story_or_path
        elif isinstance(story_or_path, str):
            story = StoryHub.get_story(story_or_path)
        story_meta = StoryHub.get_story_meta(story_or_path)
        story_meta = _generate_autodocs_base(story, story_meta)
        return story_meta


def _set_indents(story_meta: Dict) -> Dict:
    indent_targets = [
        "render_name",
        "docs",
        "type_hints",
        "result",
    ]
    for key, value in story_meta.items():
        if key in indent_targets:
            story_meta[key] = set_indent(value)

    return story_meta


def _generate_autodocs_base(story: Story, story_meta: StoryMeta) -> StoryMeta:
    if story.kwargs:
        story_meta.result = str(story.func(**story.kwargs))
    else:
        story_meta.result = str(story.func())
    return story_meta


def _clean_story_meta(story_meta):
    cleaned = {}
    for key, value in story_meta.items():
        if value:
            cleaned[key] = value

    return cleaned
