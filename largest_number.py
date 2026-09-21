n=int(input("Enter number of elements in array: "))
arr=[]
for i in range(n):
    num=int(input(f"Enter {i+1} element in array: "))
    arr.append(num)

print(arr)
largest=arr[0]
smallest=arr[0]
for i in range(1,n):
    largest=max(largest,arr[i])
    smallest=min(smallest,arr[i])
print("LARGEST NUMBER: ",largest)
print("SMALLEST NUMBER: ",smallest)
arr.sort(reverse=True)
print("Second largest: ",arr[1])
