words = ("apple", "banana", "apple", "orange", "banana", "apple")

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)