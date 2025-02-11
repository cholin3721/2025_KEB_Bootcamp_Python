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
cnt = 0
for i in range(1, num + 1, 1) :
      if num % i == 0 :
            cnt = cnt + 1

if cnt == 2 :
      print(f"{num} is Prime Number")
else :
      print(f"{num} is NOT Prime Number")