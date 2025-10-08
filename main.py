from utils import add_contact, search_contact, remove_contact

phone_list = [{'name': 'Байрас ', 'phone': '89373469604', 'favorite': True}, {'name': 'Шамиль', 'phone': '5865445582', 'favorite': False}, {'name': 'Эльвина ', 'phone': '893745855', 'favorite': False}, {'name': 'Амир', 'phone': '89374568522', 'favorite': True}]


def show_contact(contact: dict):
    print("-----------------------------------")
    print("Имя: ", contact["name"])
    print("Телефон: ", contact["phone"])
    if contact["favorite"]:
        print("Избранный: Да")
    else:
        print("Избранный: Нет")


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
        name = input("Введите имя контакта: ")
        phone = input("Введите телефона контакта: ")
        favorite = input("Введите y/n если контакт - избранный: ")

        if favorite == 'y':
            favorite = True
        else:
            favorite = False

        phone_list = add_contact(phone_list, name, phone, favorite)
    elif command == "3":
        search_name = input("Введите имя контакта или номер телефона: ")
        searched_contact = search_contact(phone_list, search_name)

        if searched_contact:
            show_contact(searched_contact)
        else:
            print('Контакт не найден')

    elif command == "4":
        search_name = input("Введите имя контакта или номер телефона: ")
        phone_list = remove_contact(phone_list, search_name)
    elif command == "0":
        break
    elif command == "1":
        for contact in phone_list:
            show_contact(contact)
    else:
        print("Введите верную команду: 1, 2, 3, 4 или 0")
