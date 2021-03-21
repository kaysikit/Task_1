x = int(input("Введите число "))
S = x
n = 0
while n != '=':
    try:
        numb = input("Введите операцию и число (Например '+ 2') ")
        if numb[0] == '+':
            n = [int(i) for i in numb.split() if i.isdigit()]
            res = n[-1]
            S += res

        elif numb[0] == '*' and numb[1] == '*':
            n = [int(i) for i in numb.split() if i.isdigit()]
            res = n[-1]
            S **= res

        elif numb[0] == '*':
            n = [int(i) for i in numb.split() if i.isdigit()]
            res = n[-1]
            S *= res

        elif numb[0] == '/':
            n = [int(i) for i in numb.split() if i.isdigit()]
            res = n[-1]
            S /= res

        elif numb[0] == '=':
            n = '='
    except:
        print("Операция введена некорректно, попробуйте ещё раз")

print(S)
