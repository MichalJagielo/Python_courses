
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(B, A):      ##class C(A, B)
    def __init__(self):
        super().__init__()

    def show(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.show()
print(C.__mro__)