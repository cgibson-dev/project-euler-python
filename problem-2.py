# Problem 2
# Even Fibonacci numbers

numA = 1
numB = 1
sum  = 0

while numA <= 4000000:
    if numA%2 == 0:
        sum += numA
    prevA = numA
    numA += numB
    numB = prevA

print('Sum:', sum)