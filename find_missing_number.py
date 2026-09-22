n=int(input("Enter number of elements in array: "))
arr=[]
for i in range(1,n+1):
    num=int(input(f"Enter value{i}: "))
    arr.append(num)

freq={}
for i in range(1,n+1):
    freq[i]=0
for num in arr:
    freq[num]=1


for key,value in freq.items():
    if(value==0):
        print(key)

