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

import math as m

num = int(input("Input Number : "))
is_prime = True
if num >= 2 :
      # for i in range(2, int(n**0.5)+1): 이것도 가능함 **은 제곱, 0.5를 제곱하면 결국은 제곱근 구하게 됨.
      for i in range(2, int(m.sqrt(num)+1)) :  #여기서 제곱근을 포함 안시키면 9 같은건 1, 3, 9 이기 때문에 3까지 검사 안하고 소수판정 내림.

            # if num % (i**2) : for문을 유지했다 했을때, i를 제곱했을때도 가능하다
            if num % i == 0 :
                  is_prime = False
                  break
else :
      is_prime=False

if is_prime :
      print(f"{num} is Prime Number")
else :
      print(f"{num} is NOT Prime Number")

print(2**10)
print(16**2)