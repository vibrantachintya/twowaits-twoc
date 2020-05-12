def isPrime(N):
    a = 2
    k = N // 2
    while k >= a:
        if N % a == 0:
            return False
        a += 1
        k = N // a
    return True

def isPalindrom(n):
    N = str(n)
    L = len(N)
    for i in range(L // 2):
        if N[i] != N[L - 1 - i]:
            return False
    return True

def isOdd(n):
    if n % 2 == 0:
        return False
    return True

def isArmstrong(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False

def check():
    number = int(input("Enter the number: "))
    if(isPrime(number)):
        print(number, "is a prime number")
    if(isOdd(number)):
        print(number, "is an odd number")
    else :
        print(number, "is an even number")
    if(isPalindrom(number)):
        print(number, "is a palindrom number")
    if(isArmstrong(number)):
        print(number, "is an armstrong number")

check()


#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH