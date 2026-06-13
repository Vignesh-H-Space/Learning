class Test:
    x = 10

a = Test()
b = Test()

a.x = 20

print(a.x)
print(b.x)
print(Test.x)