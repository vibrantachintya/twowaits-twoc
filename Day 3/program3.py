def duplicate(string):
    duplicateString = ""
    for x in string:
        if x not in duplicateString:
            duplicateString += x
    return duplicateString

string = input("Enter the string: ")
print("String after removing the duplicates is:", duplicate(string))


#code contributed by Aman Mishra (https://github.com/amanmishra2391), 2nd IT AITH