# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
#Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

num = randint(0, 1000)

attempts = 10

print("Угадайте целое число от 0 до 1000.  У вас есть 10 попыток.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Попытка {attempt}. Угадайте число: "))
    
    if guess < num:
        print("Ваше число меньше, чем задумал компьютер")
    elif guess > num:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print(f"Вы угадали число {num} за {attempt} попыток.")
        break

if guess != num:
    print(f"К сожалению, вы не угадали число. Было загадано число {num}.")