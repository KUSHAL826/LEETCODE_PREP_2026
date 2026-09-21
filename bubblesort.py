n=int(input("Enter number of elements in array: "))
arr=[]
for i in range(n):
    num=int(input(f"Enter {i+1} element in array: "))
    arr.append(num)

print(arr)

for i in range(n-1):
    for j in range(n-1-i):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
