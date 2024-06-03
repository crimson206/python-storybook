from typing import Dict


def build_template(story_meta: Dict):
    template = session_base
    template += render_name_base

    for key, value in additional_bases.items():
        if key in story_meta.keys():
            template += value

    template += result_base

    return template


session_base = """## {title}/{name}
```markdown
"""

render_name_base = """Render Name :
{render_name}

"""

docs_base = """Documentation :
{docs}

"""

type_hints_base = """Type Hints :
{type_hints}

"""

result_base = """Result:
{result}
```
"""

additional_bases = {
    "docs": docs_base,
    "type_hints": type_hints_base,
}
