def show_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data():
    fio = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {phone_number}')
    print('Успешно!')

def find_data():
    data = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        phone_book = f.read()
    print('Результаты поиска: ')
    print(search(phone_book, data))

def search(book: str, info: str):
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def edit_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        phone_book = f.read()
    phone_book = phone_book.split('\n')
    num = int(input('Введите номер записи, которую хотите изменить: '))
    phone_book[num] = edited(phone_book[num])
    phone_book = '\n'.join(phone_book)
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(phone_book)
    print(phone_book)

def edited(text: str):
    fio = input('Введите ФИО: ')
    number = input('Введите номер телефона: ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(number) == 0:
        number = text.split(' | ')[1]
    return f'{fio} | {number}'

def del_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        phone_book = f.read()
    phone_book = phone_book.split('\n')
    num = int(input('Введите номер записи, которую хотите удалить: '))
    phone_book.pop(num)
    phone_book = '\n'.join(phone_book)
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(phone_book)
    print(phone_book)