string_1 = -1
string_2 = 1
ostacha = 1
while string_1 < 0 or ostacha != 0:
    string_1 = float(input("Введите значение n! = "))
    ostacha = string_1 % 1
    if ostacha != 0:
        print("Должно быть целое числом")
    if string_1 < 0:
        print("Число должно быть > или = 0")
string_1 = int(string_1)
for i in range(1, string_1 + 1):
    string_2 = string_2 * i
print("Факториал ", string_1, "! = ", string_2)