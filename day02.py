# for dan in range(2 , 10, 1) :
#     for i in range (1, 10, 1) :
#         print(f"{dan} * {i} = {dan*i}")
#     print()
# 구구단

# dan = int(input("단을 입력하시오 : "))
# for i in range (1, 10, 1) :
#       print(f"{dan} * {i} = {dan*i}")
# print()
# 입력받은 숫자의 구구단

def is_prime(num) -> bool: # 보통 이렇게 명시적으로 써서 가독성을 높임
      """
      this function is for judge PrimeNumber, if return is true, it is.
      :param num: integer number
      :return: boolean
      """
      if num >= 2:
          i = 1
          while i > num**0.5 :
              if num % i == 0 :
                  return False
              i = i + 1
      else:
            return False

      return True

help(abs)  # help 함수의 대한 설명을 출력해주는 함수 처음알았음..
help(is_prime)  # 내가 만든 함수도 됨 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이건 몰랐네 ''' ''' 여기 안에 있는 것들이 출력됨

num = int(input("Input Number : "))

if is_prime(num):
      print(f"{num} is Prime Number")
else :
      print(f"{num} is NOT Prime Number")

# solid(srp, ocp, lsp, isp,dip) 객체 지향 프로그래밍 5대 원칙
# srp : 하나의 함수의 하나의 기능만 넣어놔야 한다. side effect = 부작용 을 걱정하기 때문