from pydantic import BaseModel
from typing import List, Any, Optional, Callable, Dict, Union
from utils import get_docs, get_type_hints
import os


class Story(BaseModel):
    name: str
    render: Callable[[Any], str]
    meta: Optional[Any]
    parent: str


class StoryMeta(BaseModel):
    title: str
    name: str
    render_name: str
    docs: str
    type_hints: Dict[str, str]


class StoryManager:
    def __init__(self, title: str):
        self.title = title
        self.meta: Any = ""
        self.stories: List[Story] = []
        self.path: str = os.path.abspath(__file__)
        StoryHub.register(story_manager=self)

    def create_story(self, story_name: str, story: str) -> None:
        story = Story(name=story_name, meta=self.meta, render=story, parent=self.title)
        self.stories.append(story)

    def get_story(self, story_name: str) -> Story:
        for story in self.stories:
            if story_name == story.name:
                return story
        raise f"There is no story named {story_name}"

    def get_story_names(self) -> List[str]:
        return [story.name for story in self.stories]


class StoryHub:
    _all_managers: List[StoryManager] = []

    @staticmethod
    def register(story_manager: StoryManager) -> None:
        if story_manager.title in StoryHub.get_titles():
            raise "Title can't be duplicated."
        else:
            StoryHub._all_managers.append(story_manager)

    @staticmethod
    def get_manager(title: str) -> StoryManager:
        for manager in StoryHub._all_managers:
            if title == manager.title:
                return manager
        raise f"There is no StoryManager with the title: {title}."

    @staticmethod
    def get_titles() -> List[str]:
        return [manager.title for manager in StoryHub._all_managers]

    @staticmethod
    def get_story(full_path: str) -> Story:
        split = full_path.split("/")
        title = "/".join(split[:-1])
        story_name = split[-1]
        story_manager = StoryHub.get_manager(title)
        story = story_manager.get_story(story_name=story_name)
        return story

    @staticmethod
    def get_story_meta(story_or_path: Union[Story, str]) -> StoryMeta:
        if isinstance(story_or_path, Story):
            story = story_or_path
        else:
            story = StoryHub.get_story(full_path=story_or_path)

        story_meta = StoryMeta(
            title=story.parent,
            name=story.name,
            render_name=story.render.__name__,
            docs=get_docs(story.render),
            type_hints=get_type_hints(story.render),
        )
        return story_meta
