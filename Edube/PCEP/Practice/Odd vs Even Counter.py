def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


nums = [12, 7, 9, 20, 33, 18]

e, o = count_even_odd(nums)

print("Even numbers:", e)
print("Odd numbers:", o)