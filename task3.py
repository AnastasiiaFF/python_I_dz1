#Напишите код, который запрашивает число и сообщает является ли оно простым или составным. \ 
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. \
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

MINIMUM = 0
MAXIMUM = 100000
num = float(input(f'Введите число от {MINIMUM} до {MAXIMUM}: '))
if num // num == 1 and num // 1 == num:
    print('введенное число является простым ')
else:
    print('число является составным ')