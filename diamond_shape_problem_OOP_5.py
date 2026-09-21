class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    def __init(self):
        print("D OBJECT CREATED")

print(D.mro())
d=D()
d.show()
