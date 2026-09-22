s={1,2,3}
s.add(1)
print(s)
#s.remove(4) raises error as 4 is not there hence if use discard() it remove if present or else it wont remove
s.discard(4)
print("Removed element",s.pop()) #removes random element
