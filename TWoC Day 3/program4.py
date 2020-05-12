def duplicate(List):
    duplicateList = []
    for x in List:
        if x not in duplicateList:
            duplicateList.append(x)
    return duplicateList

size = int(input("Enter the no of elements you want to add in List: "))
print("Enter the element in List one by one")
List = []
for i in range(size):
    List.append(input())
print("List after removing the duplicates is:", duplicate(List))

#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH