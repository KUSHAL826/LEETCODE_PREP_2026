def remove_duplicates(arr):
    n=len(arr)
    if(n==1):
        return arr
    i=0
    j=i+1
    count=0
    while(j<n):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            count+=1
        j+=1
    return arr[:count+1]

arr=[1,1]
arr=remove_duplicates(arr)
print(arr)
