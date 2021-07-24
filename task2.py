a=int(input("Enter a 1 number: "))
b=int(input("Enter a 2 number: "))
large=[]
small=[]
def compareMe(a,b):
    if a>b:
        large.append(a)
        small.append(b)
    else:
        small.append(a)
        large.append(b)
    # return large,small

print(compareMe(a,b))
print(large)
print(small)