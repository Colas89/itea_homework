num_nach = ""
num_kon = ""
rezult = 0
ostat = 1
while num_nach == "" or ostat != 0:
    num_nach = ""
    num_nach = input("Введите первое целое число:  ")
    if num_nach == "":
        continue
    num_nach = float(num_nach)
    if num_nach < 0:
        print("Значение должно > или = 0")
        continue
    ostat = num_nach % 1
    if ostat != 0:
        print("Должно быть целое число")
        continue
num_nach = int(num_nach)
ostat = 1
while num_kon == "" or ostat != 0:
    num_kon = ""
    num_kon = input("Введите второе целое число:  ")
    if num_kon == "":
        continue
    num_kon = float(num_kon)
    if num_kon < num_nach:
        print("Значение должно быть > или = числу второму числу")
        continue
    ostat = num_kon % 1
    if ostat != 0:
        print("Значение должно быть целым числом")
        continue
num_kon = int(num_kon)
print("Начало ряда - ", num_nach)
print("Конец ряда - ", num_kon)
for i in range(num_nach, num_kon + 1):
    rezult = i + rezult
    i += 1
print("Сумма чисел выбранного ряда равна: ", rezult)