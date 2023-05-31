import model

def main():
    while True:
        print(' 1. Вывод телефонной книжки\n 2. Добавление абонента в телефонную книгу\n 3. Поиск абонента в телефонной книге\n 4. Редактирование данных в телефонной книге\n 5. Удаление данных абонента из телефонной книги\n 0. Выход из телефонной книги')
        mode = int(input())
        if mode == 1:
            model.show_data() # если записной книжки нет, добавить вывод: у вас нет записной книжки
        elif mode == 2:
            model.add_data()
        elif mode == 3:
            model.find_data()
        elif mode == 4:
            model.edit_data()
        elif mode == 5:
            model.del_data()
        elif mode == 0:
            print('До новых встреч!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue