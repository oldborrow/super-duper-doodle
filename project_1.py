import random
import sys

print("Подбираем имена\n")
name = ("Александр", "Иван", "Фёдор", "Пётр", "Дмитрий", "Геннадий", "Анатолий", "Андрей")
surname = (
    'Иванов', "Сидоров", "Петров", "Александров", "Двинятин", "Козлов", "Борщенков", "Белозёров", "Брейтенбихтер",
    "Аскеров", "Друзь")
while True:
    random_name_for_printing = random.choice(name)
    random_surname_for_printing = random.choice(surname)
    print("{} {}".format(random_name_for_printing, random_surname_for_printing), file=sys.stderr)
    try_again = input("\n\nСгенерировать имя ещё раз? (Нажмите Enter для продолжения, либо напишите no)")
    if try_again.lower() == "no":
        break
