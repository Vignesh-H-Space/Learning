text = "PCEP"

result = []

for ch in text:
    result.append((ch, text.index(ch)))

result.sort(reverse=True)

for item in result:
    print(item[0], item[1])