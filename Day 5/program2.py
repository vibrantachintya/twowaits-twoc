def replaceGreatestInteger(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
size = int(input("Enter the size of the list: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("The list after replacing every element with greatest element on right side is: ", replaceGreatestInteger(List))

#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH