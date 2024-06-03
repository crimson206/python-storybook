import inspect
import typing
import os


def get_docs(func):
    return inspect.getdoc(func)


def get_type_hints_inspect(func):

    signature = inspect.signature(func)
    type_hints = {
        name: param.annotation for name, param in signature.parameters.items()
    }
    type_hints["return"] = signature.return_annotation
    return type_hints


def get_type_hints_typing(func):
    type_hints = typing.get_type_hints(func)
    return type_hints


def get_type_hints(func):
    type_hints = get_type_hints_typing(func)
    type_hints = {key: value.__name__ for key, value in type_hints.items()}
    return type_hints


def run_stories_scripts(stories_dir):
    # 'stories' 디렉토리가 실제로 존재하는지 확인
    if os.path.exists(stories_dir):
        # 해당 디렉토리로 작업 디렉토리 변경
        os.chdir(stories_dir)

        # 디렉토리 내의 모든 파일을 반복 처리
        for filename in os.listdir("."):
            if filename.endswith("stories.py"):
                print(f"Executing {filename}...")
                with open(filename, "r") as file:
                    script_content = file.read()
                    # 스크립트 실행
                    exec(script_content)
    else:
        print(f"Directory not found: {stories_dir}")
