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
            # for i in range(2, math.sqrt(num)+1): 이것도 가능함 **은 제곱, 0.5를 제곱하면 결국은 제곱근 구하게 됨.
            for i in range(2, int(num**0.5 + 1)):  # 여기서 제곱근을 포함 안시키면 9 같은건 1, 3, 9 이기 때문에 3까지 검사 안하고 소수판정 내림.
                   # if num % (i**2) : for문을 유지했다 했을때, i를 제곱했을때도 가능하다
                  if num % i == 0:
                        # is_prime = False
                        # break
                        return False
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

print(2**10)
print(16**2)

# solid(srp, ocp, lsp, isp,dip) 객체 지향 프로그래밍 5대 원칙
# srp : 하나의 함수의 하나의 기능만 넣어놔야 한다. side effect = 부작용 을 걱정하기 때문