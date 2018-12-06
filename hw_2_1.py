string_1 = ''
while string_1 == '' or string_1 == '0':
    string_1 = input("Введите первое число: ")
string_1 = float(string_1)
string_2 = float(input("Введите второе число: "))
string_3 = float(input("Введите третье число: "))

if string_2 < 0 < string_3 and string_1 != 0:
    print("{}(X**2){}x+{}=0".format(string_1, string_2, string_3))
elif string_2 < 0 and string_3 < 0 and string_1 != 0:
    print("{}(X**2){}x{}=0".format(string_1, string_2, string_3))

elif string_2 < 0 < string_3 and string_1 == 0:
    print("{}x+{}=0".format(string_2, string_3))
elif string_2 < 0 and c < 0 and string_1 == 0:
    print("{}x{}=0".format(string_2, string_3))
elif string_2 < 0 and string_1 != 0 and string_3 == 0:
    print("{}(X**2){}x=0".format(string_1, string_2))

if string_1 == 0 and string_3 == 0:
    print(string_2, "x=0")


if string_2 > 0 and string_3 > 0 and string_1 != 0:
    print("{}(X**2)+{}x+{}=0".format(string_1, string_2, string_3))
elif string_2 > 0 > string_3 and string_1 != 0:
    print("{}(X**2)+{}x{}=0".format(string_1, string_2, string_3))

elif string_2 > 0 < string_3 and string_1 == 0:
    print("{}x+{}=0".format(string_2, string_3))
elif string_2 > 0 > string_3 and string_1 == 0:
    print("{}x{}=0".format(string_2, string_3))

elif string_2 > 0 and string_1 != 0 and string_3 == 0:
    print("{}(X**2)+{}x=0".format(string_1, string_2))

elif string_2 == 0 and string_3 == 0:
    print(string_1, "(x**2)=0")


diskr = string_2**2 - 4 * string_1 * string_3
print("Дискриминант равен ", diskr)

x1 = (-string_2 + diskr**(1/2))/(2 * string_1)
x2 = (-string_2 - diskr**(1/2))/(2 * string_1)

if diskr < 0:
    print("Уравнение имеет комплексные корни:\n x1 = ", x1, "\n x2 = ", x2)
elif diskr == 0:
    print("Уравнение имеет один корень: \n", "x = ", x1)
else:
    print("Корни уравнения:\n x1 = ", x1, "\n x2 = ", x2)

