def num(n):
    string = ""
    for x in range(n):
        string+=str(x+1)
    return(string)
    
n = int(input())
print (num(n))

