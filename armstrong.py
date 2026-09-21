n=int(input("Enter number: "))
ori_num=n
arm_num=0
while(n>0):
    last_digit=n%10
    arm_num+=last_digit**3
    n=n//10

if(ori_num==arm_num):
    print("ARMSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")
