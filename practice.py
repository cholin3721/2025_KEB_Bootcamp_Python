# 정수로 이루어진 리스트 numbers가 주어진다.
# 이 리스트를 홀수는 오름차순, 짝수는 내림차순으로 정렬하여 출력하는 코드를 작성하라.
# 단, 홀수끼리의 순서는 유지하고, 짝수끼리의 순서도 유지해야 한다.
#
# 📌 제약 조건:
#
# numbers 리스트에는 홀수와 짝수가 섞여 있음.
# 새로운 리스트를 만들어도 되고, 기존 리스트를 변경해도 됨.
# 리스트 길이는 최대 1000개.

numbers = [1,3,5,6,54,3]
numbers_odd = sorted([num for num in numbers if num % 2 == 0])
odd_index = [i for i, num in enumerate(numbers) if num % 2 == 0]
numbers_even = sorted([num for num in numbers if num % 2 != 0], reverse= True)
even_index = [i for i, num in enumerate(numbers) if num % 2 != 0]

for j in odd_index :
    numbers[j] = numbers_odd[j]
for k in even_index :
    numbers[k] = numbers_even[k]