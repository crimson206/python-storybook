from pydantic import BaseModel
from typing import List, Any, Optional, Callable, Dict, Union
from .utils import get_docs, get_type_hints
import os


class Story(BaseModel):
    name: str
    func: Callable[[Any], Any]
    meta: Optional[Any]
    parent: str
    kwargs: Optional[Dict[str, Any]]


class StoryMeta(BaseModel):
    title: str
    name: str
    func_name: str
    docs: Optional[str]
    type_hints: Optional[Dict[str, str]]
    result: Optional[str] = None


class StoryManager:
    def __init__(self, title: str):
        self.title = title
        self.meta: Any = ""
        self.stories: Dict[str, Story] = {}
        self.path: str = os.path.abspath(__file__)
        StoryHub.register(story_manager=self)

    def create_story(
        self,
        story_name: str,
        func: Callable[[Any], str],
        kwargs: Optional[Dict[str, str]] = None,
    ) -> None:
        story = Story(
            name=story_name,
            meta=self.meta,
            func=func,
            parent=self.title,
            kwargs=kwargs,
        )
        self.stories[story_name] = story

    def get_story(self, story_name: str) -> Story:
        if story_name in self.stories.keys():
            return self.stories[story_name]
        raise f"There is no story named {story_name}"

    def get_story_names(self) -> List[str]:
        return list(self.stories.keys())

    def get_story_full_paths(self) -> List[str]:
        return [self.title + "/" + story_name for story_name in self.stories.keys()]

    def get_stories(self):
        return list(self.stories.values())


class StoryHub:
    _all_managers: Dict[str, StoryManager] = {}

    @staticmethod
    def register(story_manager: StoryManager) -> None:
        # To preven it, we need the path of each stories.
        # if story_manager.title in StoryHub.get_titles():
        #    raise "Title can't be duplicated."
        # else:
        StoryHub._all_managers[story_manager.title] = story_manager

    @staticmethod
    def get_manager(title: str) -> StoryManager:
        for manager_title, manager in StoryHub._all_managers.items():
            if title == manager_title:
                return manager
        raise f"There is no StoryManager with the title: {title}."

    @staticmethod
    def get_titles() -> List[str]:
        titles = list(StoryHub._all_managers.keys())
        return titles

    @staticmethod
    def get_all_story_full_paths() -> List[str]:
        paths = []
        for manager in StoryHub._all_managers.values():
            paths.extend(manager.get_story_full_paths())
        return paths

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
        elif isinstance(story_or_path, str):
            story = StoryHub.get_story(full_path=story_or_path)
        else:
            raise "invalid input."

        story_meta = StoryMeta(
            title=story.parent,
            name=story.name,
            func_name=story.func.__name__,
            docs=get_docs(story.func),
            type_hints=get_type_hints(story.func),
        )
        return story_meta
