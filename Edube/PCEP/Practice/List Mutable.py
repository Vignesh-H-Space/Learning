data = [1, 2, 3, 4]

def mystery(lst):
    lst.append(lst[-1] * 2)
    lst.insert(1, lst[0] + lst[2])
    return lst

result = mystery(data)

print("data:", data)
print("result:", result)