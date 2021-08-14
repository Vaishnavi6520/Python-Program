a=int(input("Enter first number: "))
even=[]
odd=[]
def evenOdd(a):
    if(a%2==0):
        even.append(a)
    else:
        odd.append(a)
evenOdd(a)
print(even)
print(odd)