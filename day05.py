def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())

def Fibonacci(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci2(n) :
    n_list = [0, 1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i+1])

def Fibonacci3(n) :
    a, b = 0, 1
    for i in range(n) :
        a, b = b, b+a
    return a

def print_Fibonacci3(n) :
    print(Fibonacci3(n)[n])


def time_bomb_recursion(n) :
    if n == 0:
        print("BAAAAAAAAAAANG!!!!!!")
        return
    else :
        print(n)
    return time_bomb_recursion(n-1)

def time_bomb_for(n) :
    for i in range(n, 0, -1) :
        print(i)
    print("BAAAAAAAAAAANG!!!!!!")


while True :
    a=int(input("Input Number : "))
    print(Fibonacci(a))
    print(Fibonacci3(a))
    time_bomb_recursion(a)
    time_bomb_for(a)