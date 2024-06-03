import json


def reculsive_rag(query: str = "hi") -> str:
    retrieved = {"file1": "Hello world.", "file2": "This is a book."}

    return json.dumps(retrieved)


def i_am_princess2():
    return "A boring sentence."
