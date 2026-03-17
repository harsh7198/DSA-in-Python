def asc(n):
    if n==0 : 
        return  
    else :
        asc(n-1)
        print(n)
num = int(input("Enter a number : "))
print(asc(num))