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

num = int(input("Input Number : "))
is_prime = True
if num >= 2 :
      for i in range(2, num) :
            if num % i == 0 :
                  is_prime = False
                  break
else :
      is_prime=False

if is_prime :
      print(f"{num} is Prime Number")
else :
      print(f"{num} is NOT Prime Number")