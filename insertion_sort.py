n=int(input("Enter number of elements in array: "))
arr=[]
for i in range(n):
    num=int(input(f"Enter {i+1} element in array: "))
    arr.append(num)

print(arr)

for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j
                           ]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print(arr)
