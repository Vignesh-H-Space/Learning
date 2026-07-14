

class A:
    def ping(self):
        return "A"

class B(A):
    def ping(self):
        # super() looks at the NEXT class in the queue, not necessarily A!
        return "B -> " + super().ping()

class C(A):
    def ping(self):
        return "C -> " + super().ping()

class D(B, C):
    def ping(self):
        return "D -> " + super().ping()

