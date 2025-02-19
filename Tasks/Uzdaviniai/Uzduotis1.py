words = ['namas', 'namelis', 'nameliukas']
result = ''
for i in range(1, len(words[1])):
    w = (words[0][:i])
    if all(word.startswith(w) for word in words):
        result = w

print(result)