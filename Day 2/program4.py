
n = int(input("Enter the Value of N: "))
for i in range(n):
    print("* " * (n - i) + "    " * i + " *" * (n - i))
for i in range(2,n + 1):
    print("* " * i + "    " * (n - i) + " *" * i)

#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH