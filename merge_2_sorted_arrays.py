i=0
j=0
arr1=[1,3,6,7]
arr2=[1,2,3,4,7,8,9]
l1=len(arr1)
l2=len(arr2)
arr=[]
while(i<l1 and j<l2):
    if(arr1[i]<=arr2[j]):
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1
while(i<l1):
    arr.append(arr1[i])
    i+=1
while(j<l2):
    arr.append(arr2[j])
    j+=1
print(arr)

count={}
for i in arr:
    if i not in count.keys():
        count[i]=1
    else:
        count[i]+=1

for key in count.keys():
    print(key,end=" ")
        
