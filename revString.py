def revStr(str1):
    result=""
    lenStr=len(str1)
    for item in range(-(lenStr-1),1,1):
        result=result+str1[item]
    return result


string1="Hello World"
print(revStr(string1))