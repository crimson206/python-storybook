from python_storybook.main import app
from python_storybook.utils import run_stories_scripts
import os

stories_dir = os.path.dirname(__file__) + '/stories'

if __name__ == "__main__":
    import uvicorn
    run_stories_scripts(stories_dir=stories_dir)

    uvicorn.run(app, host="0.0.0.0", port=8000)
