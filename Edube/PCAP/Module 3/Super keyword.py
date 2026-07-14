

class A:
    def ping(self):
        return "A"

class B(A):
    def ping(self):
        # super() looks at the NEXT class in the queue, not necessarily A!
        return "B -> " + super().ping()
