n=int(input("Enter number: "))
n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
Emty=[n,n1,n2]
def sqr(n):
    return n**2
print(list(map(sqr,Emty)))