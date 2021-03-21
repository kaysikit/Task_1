text = input("Введите текст")
text.replace(" ", "")
a = o = u = i = e = y = 0
for el in text:
    if el == 'a':
        a += 1
    elif el == 'o':
        o += 1
    elif el == 'u':
        u += 1
    elif el == 'i':
        i += 1
    elif el == 'e':
        e += 1
    elif el == 'y':
        y += 1
print(f'a - {a}, o - {o}, u - {u}, i - {i}, e - {e}, y - {y}')
