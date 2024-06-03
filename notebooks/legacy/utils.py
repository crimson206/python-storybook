import inspect
import typing


def get_docs(func):
    return inspect.getdoc(func)


def get_type_hints_inspect(func):

    signature = inspect.signature(func)
    type_hints = {
        name: param.annotation
        for name, param
        in signature.parameters.items()
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
