def reverse_string(text):
    result = ""

    for ch in text:
        result = ch + result

    return result


print(reverse_string("python"))  