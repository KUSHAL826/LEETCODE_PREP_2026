arr=[1,2,3,4,5]
k=3
n=len(arr)

rotations=k%n
"""
for i in range(0,rotations):
    e=arr.pop()
    arr.insert(0,e)

print(arr)
"""
arr[:]=arr[n-k:]+arr[:n-k]
print(arr)
