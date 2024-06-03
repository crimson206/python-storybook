from core import StoryManager
from stories.some_script import default

stories = StoryManager("Example")

stories.create_story(
    story_name="Sample",
    story=default
)

print(default)
