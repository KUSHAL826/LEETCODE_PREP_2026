n=int(input("Enter length of array: "))
arr=[]
for i in range(n):
    elem=int(input(f"Enter element{i+1}: "))
    arr.append(elem)
print(arr)
#brute force
"""new_arr=[]
count=0
for i in range(n):
    if arr[i]!=0:
        new_arr.append(arr[i])
        count+=1

while(count<n):
    new_arr.append(0)
    count+=1

arr=new_arr
print(arr)
"""
#optimal
j=0
for i in range(n):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

print(arr)
