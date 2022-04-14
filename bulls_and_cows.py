from random import randint
# Підключення модуля random


def is_valid(n):
    # Перевіряємо чи введена строка - чотиризначне число
    while not n.isdigit() or len(n) != 4:
        n = input('Введіть чотирьохзначне число!\n')
    return n


def play(real_number):
    c = 0
    # print(real_number)

    while True:
        print()
        guess = is_valid(input('Введіть чотиризначне число:\n'))  # Перевірка
        print()

        c += 1  # додаємо 1 до лічильника спроб
        bull = 0
        cow = 0

        for i in range(4):
            if guess[i] in real_number and guess[i] == real_number[i]:
                bull += 1  # к-сть биків, якщо цифра є у числі та вона на своєму місці
            elif guess[i] in real_number and not guess[i] == real_number[i]:
                cow += 1   # к-сть корів, якщо цифра є у числі та вона не на своєму місці

        if guess == real_number:
            print('Це правильне число!')
            break  # Обриваємо цикл, коли число вгадане
            
        print(f'Введене число: {guess}')
        print(f'Бики: {bull}, Корови: {cow}')
        print(f'Спроб: {c}')  # Виводимо дані


# Компьютер загадує чотиризначне число з різними цифрами
number = ''
while len(number) != 4:
    r = str(randint(1, 9))
    if r not in number:
        number += str(r)

# Опис гри
print('Це гра "Бики та корови"\n')
print('Потрібно відгадати чотиризначне число\n')
print('Після кожної спроби показується к-сть корів та биків\n')
print('Бики - к-сть цифр, що збігаються та стоять на свому місці\n',
      'Корови - к-сть цифр, що є в задуманому числі, але стоять не на своєму місці', sep='\n')

play(number)
