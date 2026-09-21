#count freqency of numbers
arr=[]
n=int(input("Enter number of elements in array: "))

for i in range(n):
    num=int(input(f"Enter element {i+1} in array: "))
    arr.append(num)
freq={}
for i in arr:
    if(i not in freq.keys()):
        freq[i]=1
    else:
        freq[i]+=1

for key,value in freq.items():
    print(f"{key} -- {value}")
    

