import random
n=random.randint(1,7) #returns number b/w 1 to 7 including 1 and 7
print(n)
n1=random.randrange(1,3) #returns number b/w and 1 and 3 excluding 3
print(n1)
n2=random.random() #returns random floating number
print(n2)
n3=random.uniform(1,3) #return random floating number in the given range
print(n3)
l=[1,23,4,54,32,54]
n4=random.choice(l)
print(n4)
random.shuffle(l)
print(l)
