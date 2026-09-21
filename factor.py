"""#brute force
n=int(input("Enter the number: "))
res=[]
for i in range(1,n):
    if(n%i==0):
        res.append(i)
res.append(n)
print("FACTORS: ",end=" ")
for r in res:
    print(r,end=" ")
"""

#optimal solution
n=int(input("Enter the number: "))
res=[]
for i in range(1,n//2+1):
    if(n%i==0):
        res.append(i)

res.append(n)
print("FACTORS: ",end=" ")
for r in res:
    print(r,end=" ")
    
