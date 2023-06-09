import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '=' * 71)
        for i, contact in enumerate(book, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20}  | {contact.get("comment"):^20}')
        print('=' * 71 + '\n')
    else:
        print_message(error)


def input_contact() -> dict[str, str]:
    new = {}
    print(text.input_new_contact)
    for key, txt in text.new_contact.items():
        new[key] = input(txt)
    return new


def input_search() -> str:
    return input(text.input_search)


def change_id(length, txt) -> int:
    result = input(txt)
    if result.isdigit() and 0 < int(result) <= length:
        return int(result)
    else:
        change_id(length, txt)
