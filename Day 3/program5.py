size1 = int(input("Enter the no of elements you want to enter in the List 1: "))
print("Enter the elements in List1 one by one")
list1 = []
for i in range(size1):
    list1.append(input())
size2 = int(input("Enter the no of elements you want to enter in the List 2: "))
print("Enter the elements in List2 one by one")
list2 = []
for i in range(size2):
    list2.append(input())
intersectionList = list(set(list1).intersection(set(list2)))
print("The intersection of List 1 and List 2 is:", ", ".join(intersectionList))


#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH