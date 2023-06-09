import view, text

phone_book: list[dict[str, str]] = []
path = 'phones.txt'


def open_pb():
    global phone_book
    with open(path, 'r', encoding="UTF-8") as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(":")
        new = {'name': contact[0], 'phone': contact[1], 'comment': contact[2]}
        phone_book.append(new)


def save_pb():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book
    phone_book.append(new)
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                result.append(contact)
                break
    return result


def delete_contact():
    global phone_book
    result: list[dict[str, str]] = []
    key_world = view.input_search()
    result = search_contact(key_world)
    view.print_contacts(result, text.empty_search(key_world))
    delete_id = view.change_id(len(result), text.delete_contact) - 1
    for contact in phone_book:
        if contact == result[delete_id]:
            phone_book.remove(contact)


def change_contact():
    global phone_book
    result: list[dict[str, str]] = []
    key_world = view.input_search()
    result = search_contact(key_world)
    view.print_contacts(result, text.empty_search(key_world))
    change_id = view.change_id(len(result), text.change_contact) - 1

    for contact in phone_book:
        if contact == result[change_id]:
            Result = view.input_contact()
            contact['name'] = Result['name']
            contact['phone'] = Result['phone']
            contact['comment'] = Result['comment']