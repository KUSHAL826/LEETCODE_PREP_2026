n=int(input("Enter lenght of array: "))
arr=[]
for i in range(n):
    num=int(input(f"Enter {i+1} element in array: "))
    arr.append(num)
print(arr)

for i in range(n):
    min=i
    for j in range(i+1,n):
        if(arr[min]>arr[j]):
            min=j
    if(min!=i):
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

print(arr)
