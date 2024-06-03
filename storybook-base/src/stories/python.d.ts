/** 
 * type is okay without global, but for interfaces.
*/

declare global {
    type py_str = string;
    type py_int = number;
    type py_float = number;
    type py_bool = boolean;

    interface py_Dict {
        [key: py_str]: any;  // 모든 키는 string, 모든 값은 any 타입
    }

    type py_List<T> = Array<T>;

    type py_Optional<T> = T | null;
}

// 이렇게 선언하면 아래의 코드로 전역 타입이 적용된다는 것을 알릴 필요가 있습니다.
export {};