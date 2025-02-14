import time

def calculate_time(func) :
    def inner_func_time(*arg) :
        s = time.perf_counter()
        result = func(*arg)
        e = time.perf_counter()
        print(f"이 함수가 가동된 시간은 {e-s}초 입니다.")
        return result
    return inner_func_time

def description(func) :
    def inner_func_descript(*arg) :
        print(func.__name__)
        print(func.__doc__)
        result = func(*arg)
        return result
    return inner_func_descript

@description
@calculate_time
def power_bomb(a, b) -> int :
    """
    :param a: int
    :param b: int
    :return: int
    """
    return a ** b

def no_decorate_power_bomb(a , b) -> int :
    """
    :param a: int
    :param b: int
    :return: int
    """
    return a ** b

print(power_bomb(3, 3))
# description(calculate_time(power_bomb))
f1 = description(calculate_time(no_decorate_power_bomb))
# print(f1(3, 3))
