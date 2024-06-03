from python_storybook.core import StoryManager
from python_storybook.stories.rag import i_am_princess, reculsive_rag

title = "Example/String"

story_manager = StoryManager(title=title)

story_manager.create_story(story_name="Custom Name", func=i_am_princess)

story_manager.create_story(story_name=reculsive_rag.__name__, func=reculsive_rag)
