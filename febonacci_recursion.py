
def febonacci(num):
    if(num==0 or num==1):
        return num
    return febonacci(num-1)+febonacci(num-2)
n=int(input("Enter number: "))
for i in range(n):
    print(febonacci(i),end=" ")

