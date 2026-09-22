nums=[1,1,0,1,1,1,1,1,0,1]
count=0
max_count=0
for num in nums:
    if num==1:
        count+=1
    else:
        count=0

    if max_count<count:
        max_count=count

print("MAXIMUM NUMBER OF CONSECUTIVE ONES: ",max_count)
