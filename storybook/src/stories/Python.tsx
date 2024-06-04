/**

type py_str = string;
type py_int = number;
type py_float = number;
type py_bool = boolean;

interface py_Dict {
    [key: py_str]: any;  // 모든 키는 string, 모든 값도 string
}

type py_List<T> = Array<T>;



type py_Optional<T> = T | null;
 */

interface GetStringProp {
    query: py_str;
}

interface GetDictProp {
    key: py_str
    value: py_float
}

const get_string = ({query}: GetStringProp): py_str => {
    return "HI"
}

const get_list = ({query}: GetStringProp): py_List<py_str> => {
    return ["HI"]
}

const get_number = ({query}: GetStringProp): py_int => {
    return 123
}

const get_boolean = ({query}: GetStringProp): py_bool => {
    return true
}

const get_dictionary = ({key: py_str, value: py_float}: GetDictProp): py_Dict => {
    return {key: 3.14}
}

const get_dictionary_optional = ({key: py_str, value: py_float}: GetDictProp): py_Optional<py_Dict> => {
    if (py_float == 1)
        {return {key: 3.14}}
    else
        {return null}
}
