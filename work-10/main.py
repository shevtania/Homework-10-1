from addressrecords import AddressBook, Record

address_book = AddressBook()

# decorator for exceptions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'

        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it already exists.'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner


#blocks for input commands:

def hello():
    result = 'How can I help you?'
    return result

@input_error
def add_contact(*args):
    name, *phones = args
    if  address_book.search_record(name):
        return 'This contact cannot be added, it already exists.'
    record = Record(name, phones)
    address_book.add_record(record)
   
    return f'Added contact: {record}'

@input_error
def add_phone(*args):
    name, phone = args
    if  not address_book.search_record(name):
        return "This phone cann't be added, contact doesn't exist."
    record = address_book.search_record(name)
    record.add_phone(phone)
    
    return f'Added {phone} in contact: {record}'

@input_error
def del_phone(*args):
    name, phone = args
    if  not address_book.search_record(name):
        return "This phone cann't be deleted, contact doesn't exist."
    record = address_book.search_record(name)
    result = record.del_phone(phone)
    
    return result

@input_error
def change_phone(*args):
    name, old_phone, new_phone = args
    record = address_book[name]
    result = record.change_phone(old_phone, new_phone)
   
    return result

@input_error
def phone_from_name(args):
    name = args[0]
    record = address_book.search_record(name)
    if not record:
        return f'This contact is not the book.'
    return record.show_all_phones() 


def  show_all_contacts():
    result = ''
    address_dict = address_book.show_all_contacts()
    if not address_dict:
        return f'There are no contacts in the book.'
        
    for record in address_dict.values():
        result = result + f'{record.show_all_phones()}\n'
        
    return result 

def exit():
    return 'exit'
    
    

HANDLERS = {
    "hello": hello,
    "good bye": exit,
    "close": exit,
    "exit": exit,
    "add contact": add_contact,
    "add phone": add_phone,
    "del phone": del_phone,
    "change": change_phone,
    "show all": show_all_contacts,
    "phone": phone_from_name
}

def parser_input(user_input):
    command, *args = user_input.split()
    handler = None
    command = command.lower()
    if command in HANDLERS:
        handler = HANDLERS[command]
    else:
        if args:
            command = command + ' ' + args[0]
            args = args[1:]
            if command in HANDLERS:
                handler = HANDLERS.get(command)
        
    return handler, *args


def main():
    while True:
        user_input = input("Input command: ")
        handler, *args = parser_input(user_input)
        if handler:
            result = handler(*args)
        else:
            result = f'Unknown command'    
        
        if result == 'exit':
            print("Good bye!")
            break
        print(result)
        


if __name__ == "__main__":

    main()
