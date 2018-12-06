string = 0
rez_a = 0
rez_b = 1
while string <= 0 or ostatok != 0:
    string = float(input("Введите номер числа Фибоначчи :"))
    ostatok = string % 1
    if ostatok != 0:
        print("Число должно быть целым")
    if string <= 0:
        print("Число должно быть > 0")
string = int(string)
for i in range(0, string + 1):
    rez_a = rez_a + rez_b
    rez_b = rez_a - rez_b
print("Номер Фибоначчи ", string, " = ", rez_b)