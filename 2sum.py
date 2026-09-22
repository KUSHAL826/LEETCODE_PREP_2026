nums=[]
n=int(input("Ente
            r array size: "))
for i in range(n):
    num=int(input(f"Enter array element{i+1}: "))
    nums.append(num)

print(nums)
target=int(input("Enter target element: "))
i=0
j=n-1
res=[]
while i<j:
    if nums[i]+nums[j]==target:
        res.append(i)
        res.append(j)
        break
    elif nums[i]+nums[j]>target:
        j-=1
    else:
        i+=1

if len(res)==0:
    print("TARGET NOT FOUND")
else:
    print(f"Target found at place {res[0]} , {res[1]}")
