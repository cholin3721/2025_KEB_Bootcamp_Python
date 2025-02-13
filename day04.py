#SOLID
#Open Closed Principle : 개방 폐쇄 원칙(확장에는 열려있고 수정에는 닫혀있다.)
# S는 단일 체계의 원칙

import time

def time_decorator (func):
    def wrapper(*args) :
        s = time.perf_counter()
        r = func(*args)
        e = time.perf_counter()
        print(f"{e-s} 초가 걸렸습니다.")
        return r
    return wrapper

@time_decorator
def factorial_repetiton(n) -> int:
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def power(b, e) :
    print(b**e)

number = int(input("Input Number : "))
# s = time.time()
print(f"{number}! = {factorial_repetiton(number)}")

power(3,5)
# e = time.time()
# print(e-s)
# print(type(e-s))