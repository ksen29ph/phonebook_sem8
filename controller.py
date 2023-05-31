import model

def main():
    while True:
        print(' 1. Вывод\n 2. Добавление абонента\n 3. Поиск абонента\n 4. Редактирование данных\n 5. Удаление данных абонента\n')
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
        else:
            break