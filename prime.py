try:
    x = int(input("Введите число "))
    k = 0
    for el in range(2, x + 1):
        if x % el == 0:
            k += 1
    if k == 1:
        print("Простое число")
    else:
        print("Не простое число")
except:
    print("Это не число")