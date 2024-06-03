import json


def reculsive_rag(query: str = "hi", more_args: int = 10) -> str:
    retrieved = {"file1": "Hello world.", "file2": "This is a book."}

    return json.dumps(retrieved)


def i_am_princess():
    return "A boring sentence."
