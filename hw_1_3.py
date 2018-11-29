# coding=utf-8
string_1 = float(input('Введите число: '))
print('1. ', int(string_1))
print('2. ', float(string_1))
print('3. ', str(string_1))
print('4. ', bool(string_1))

print('------------------')

string_2 = float(input('Введите второе число: '))
print(int(string_1) + string_2)
print(int(string_1) * string_2)

print('------------------')

print(int(string_1) + int(string_2))
print(int(string_1) * int(string_2))

print('------------------')

print(string_1 + string_2)
print(string_1 * string_2)

print('------------------')

print(str(string_1) + str(string_2))

print('------------------')

print(bool(string_1) + bool(string_2))
print(bool(string_1) * bool(string_2))

print('------------------')

print(float(string_1) + bool(string_2))
print(float(string_1) * bool(string_2))

print('------------------')


print(int(string_1) + bool(string_2))
print(int(string_1) * bool(string_2))
print('------------------')

print(str(string_1) * bool(string_2))
