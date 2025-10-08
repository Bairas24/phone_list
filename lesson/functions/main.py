phone_list = [{'name': 'Байрас ', 'phone': '89373469604', 'favorite': True}, {'name': 'Шамиль', 'phone': '5865445582', 'favorite': False}, {'name': 'Эльвина ', 'phone': '893745855', 'favorite': False}, {'name': 'Амир', 'phone': '89374568522', 'favorite': True}]


def show_contact():
    for contact in phone_list:
        print("-----------------------------------")
        print("Имя: ", contact["name"])
        print("Телефон: ", contact["phone"])
        if contact["favorite"]:
            print("Избранный: Да")
        else:
            print("Избранный: Нет")


def add_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите телефона контакта: ")
    favorite = input("Введите y/n если контакт - избранный: ")

    if favorite == 'y':
        favorite = True
    else:
        favorite = False

    contact = {
        "name": name,
        "phone": phone,
        "favorite": favorite
    }

    phone_list.append(contact)


def remove_contact():
    name_for_remove = input("Введите имя контакта: ")

    is_founded = False
    for contact in phone_list:
        if contact["name"] == name_for_remove:
            is_founded = True
            phone_list.remove(contact)
            print('Контакт удален: ', name_for_remove)

    if is_founded == False:
        print('Контакт ранее был удален')


def search_contact():
    search_name = input("Введите имя контакта: ")

    is_founded = False
    for contact in phone_list:
        if contact["name"] == search_name:
            is_founded = True
            print('Контакт найден: ', contact)

    if is_founded == False:
        print('Контакт ранее был удален')

while True:
    print("===================================")
    print("1. Показать все")
    print("2. Добавить")
    print("3. Найти")
    print("4. Удалить")
    print("0. Выход")
    print("===================================")
    command = input("Выберите команду: ")

    if command == "2":
        add_contact()
    elif command == "3":
        search_contact()
    elif command == "4":
        remove_contact()
    elif command == "0":
        break
    elif command == '1':
        show_contact()
    else:
        print("Введите верную команду: 1, 2, 3, 4 или 0")

На прошлом уроке с учеником разобрали данный код

Он был очень полезным и понравилось что я составл ТЗ
За это спасибо

Идем дальше
Теперь нам предстоит 2 часа обучения
Я хочу вначале углубиться в функции на этом же примрее (чтобы аогрменты и return понять)

Дальше уже надо думать - либо классы, либо идем к проекту

Как ты считаешь что лучше?

Мы должны начать приступить к написанию своег опроекта закрыв ознакомление с основыми пайтон - чтобы он после портфолио шел на трудоустройство