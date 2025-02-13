#SOLID
#Open Closed Principle : 개방 폐쇄 원칙(확장에는 열려있고 수정에는 닫혀있다.)
# S는 단일 체계의 원칙

def factorial_repetiton(n) -> int:
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input("Input Number"))
print(f"{number}! = {factorial_repetiton(number)}")