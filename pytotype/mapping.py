'''
| Python       | TypeScript  |
|--------------|-------------|
| `int`        | `number`    |
| `float`      | `number`    |
| `str`        | `string`    |
| `bool`       | `boolean`   |
| `list`       | `Array<T>`  |
| `dict`       | `{ [key: string]: T }` |
| `tuple`      | `[type1, type2, ...]`  |
| `Set`        | `Set<T>`    |
| `None`       | `null` or `undefined`  |
'''

from pydantic import BaseModel


basic_mappings = [
    {'python':"str", "typescript":"string"},
]

generic_mappings = [
    {'python':'List[T]', "typescript":"Array<T>"},
]
