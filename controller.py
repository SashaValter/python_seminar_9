import text
import view
import model


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact()
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_world = view.input_search()
                result = model.search_contact(key_world)
                view.print_contacts(result, text.empty_search(key_world))
            case 6:
                model.change_contact()
                view.print_message(text.change_successful)
            case 7:
                model.delete_contact()
                view.print_message(text.delete_successful)
            case 8:
                break