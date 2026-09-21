#extracting last digit , finding reverse number
length=0
n=int(input("Enter number: "))
ori_num=n
rev=""

while(n>0):
    last_digit=n%10
    rev+=str(last_digit)
    n=n//10
    length+=1
rev=int(rev)
print("REVERSED NUMBER: ",rev)
print("LENGHT OF GIVEN NUMBER: ",length)

if(ori_num==rev):
    print("PALINDROME NUMBER")
else:
    print("NOT A PALINDROME NUMBER")

