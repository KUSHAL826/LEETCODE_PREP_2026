n=int(input("Enter number of elements in array: "))
arr=[]
for i in range(n):
    num=int(input(f"Enter {i+1} element in array: "))
    arr.append(num)

print(arr)
"""freq={}
for i in range(n):
    if arr[i] in freq.keys():
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
print(freq)
for key in freq.keys():
    print(key,end=" ")
"""
for i in range(n):
    if(arr[i]!=arr[i+1]):
        arr[i+1
