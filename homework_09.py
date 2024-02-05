def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {e}"
        except ValueError:
            return "Error: Invalid input format. Please provide name and telephone number."
        except IndexError:
            return "Error: Index out of range."
    return wrapper


def hello_command():
    return 'How can I help you?'

@input_error
def add_command(contacts, input_command):
    _, name, phone = input_command.split()
    if name not in contacts:
        contacts[name] = phone
        return f'Contact {name} added.'
    else:
        return f'This name already exists.'

@input_error
def change_command(contacts, input_command):
    _, name, phone = input_command.split()
    if name.lower() in contacts:
        contacts[name] = phone
        return f'Phone number for {name}, changed.'
    else:
        return 'Such a name does not exist.'

@input_error
def phone_command(contacts, input_command):
    _, name = input_command.split()
    if name.lower() in contacts:
        return f'Phone number for {name}: {contacts[name]}.'
    else:
        return 'Such a name does not exist.'

@input_error
def show_all_command(contacts):
    if not contacts:
        return 'Contacts not found.'
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}

    while True:
        user_input = input('Enter command: ').lower()

        if user_input == '.':
            print('Good bye!')
            break

        if user_input in ['good bye', 'close', 'exit']:
            print('Good bye!')
            break

        if user_input.startswith('hello'):
            print(hello_command())

        elif user_input.startswith('add'):
            print(add_command(contacts, user_input))

        elif user_input.startswith('change'):
            print(change_command(contacts, user_input))

        elif user_input.startswith('phone'):
            print(phone_command(contacts, user_input))

        elif user_input.startswith('show all'):
            print(show_all_command(contacts))

        else:
            print("Error: Invalid command. Please try again.")


if __name__ == '__main__':
    main()
