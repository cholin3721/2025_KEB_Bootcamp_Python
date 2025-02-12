# prime number
import math as m


def my_pow(num1, num2) -> float:
    '''
    :param num1  : basenumber
    :param num2  : exponent
    :return float: the power result iin the form of a real number
    alternate the pow()
    '''

    result = 1


    i = int(num2)
    f = num2 - i
    # for _ in range(num2) :
    for _ in range(i):
        result *= num1

    if f > 0:
        result = result * m.exp(f * m.log(num1))

    return result


# 함수와 함수 사이는 2줄 띄는게 국룰
# def is_prime(n1) -> bool :
#     '''
#     :param n1 int:
#     :return:
#
#     '''
#     i = 2
#     while my_pow(i, 2) <= n1:
#         if n1 % i == 0:
#             return False
#         i = i + 1
#     return True
#
# numbers = input("Input first second number ex -> 15 24) : ").split()
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2 :
#     n1, n2 = n2, n1
#
# while n1 <= n2 :
#     if is_prime(n1) :
#         print(n1, end=" ")
#     n1 += 1

# print(m.exp)
# print(m.e)
# print(m.log())
# exp() : 오일러수 자연상수 네이피어상수 << 이거 공부해봐야하나
# log() : 로그함수

print(my_pow(2, 9))
print(my_pow(16, 0.5))
print(my_pow(10, 3))
print(my_pow(25, 0.5))

