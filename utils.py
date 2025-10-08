def add_contact(phone_list: list, name: str, phone: str, favorite: bool) -> list:
    contact = {
        "name": name,
        "phone": phone,
        "favorite": favorite,
    }

    phone_list.append(contact)

    return phone_list

def add_contact(phone_list: list, name: str, phone: str, favorite: bool) -> list:
    contact = {
        "name": name,
        "phone": phone,
        "favorite": favorite,
    }

    phone_list.append(contact)

    return phone_list


def search_contact(phone_list: list, search: str) -> dict | None:
    for contact in phone_list:
        if search == contact['name'] or search == contact['phone']:
            return contact
    return None


def remove_contact(phone_list: list, search: str) -> list:
    searched_contact = search_contact(phone_list, search)

    if searched_contact:
        phone_list.remove(searched_contact)
    return phone_list

deleted_phone_list = []



