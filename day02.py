# prime number

numbers = input("Input first second number ex -> 15 24) : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2 :
    n1, n2 = n2, n1

else :
    pass

while n1 <= n2 :
    i = 2
    is_Prime = True
    while pow(i, 2) <= n1 :
        if n1 % i == 0 :
            is_Prime = False
            break
        i = i + 1
    if is_Prime :
        print(n1, end=" ")
    n1 = n1 + 1
