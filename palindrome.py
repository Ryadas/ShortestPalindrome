import string
alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)]) + string.ascii_lowercase
letters = ''.join(elem.lower() for elem in input() if elem.lower() in alphabet)  # удаление сторонних элементов
n, pals = len(letters), []

for i in range(n):
    word = letters[i]
    for j in range(i + 1, n):
        word = word + letters[j]
        if word == word[::-1]:
            pals.append(word)
            break
            
print(sorted(sorted(pals), key=lambda x: len(x))[0])

