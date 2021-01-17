class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")


class C(A):
    def m(self):
        print("m of C called")


class D(C, B):
    def m(self):
        print("m of D called")


print(D.mro())

d = D()
d.m()
