from collections import UserDict

class Field():
    def __init__(self, value) -> None:
        self.value = value

class Name(Field):
    pass
      

class Phone(Field):

    def __eq__(self, other):
       return self.value == other.value
    
    def __str__(self) -> str:
        return self.value
             
     

class Record():
    def __init__(self, name: str, args):
        self.name = Name(name)
        self.phone_list = []
        for phone in args:
            self.phone = Phone(phone)
            self.phone_list.append(self.phone)
      
    def add_phone(self, phone):
        self.phone_list.append(Phone(phone))
        return  

    def del_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phone_list:
            self.phone_list.remove(phone) 
            return  f'{phone} in contact is deleted.'
        return 'This phone doesnt exist, please try again.'
        
    def change_phone(self, old_phone, new_phone):
        if Phone(old_phone) in self.phone_list:
            self.phone_list.remove(Phone(old_phone))
            self.phone_list.append(Phone(new_phone))       
            return "Phone changed"
        return "This contact doesn't exist, please try again."  
    
    def  show_all_phones(self):
        phones = ', '.join(str(p) for p in self.phone_list)
       
        return f'{self.name.value}: {phones}'
    
    def __str__(self) -> str:
        return self.show_all_phones()

class AddressBook(UserDict):
    def __init__(self):
        pass
      
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return 
        
    def search_record(self, name):
        return self.data.get(name)   
    
    def show_all_contacts(self):
        return self.data


# tests for classes:
#
#name = Name('U')
#record = Record('N', '54685', '12', '34')
#record = Record("N")
#phone = Phone('1234567')
#print(record.add_phone(phone))
#print(record.del_phone('12'))
#print(record.add_phone('343434872934'))
#print(record.add_phone('1'))
#print(record.change_phone('343434872934', '9876543'))
#print(record.show_all_phones())
#adress = AddressBook()
#print(adress.add_record(record))
#print(adress.data)
#print(record.del_phone('13'))
#print(record.change_phone('343434872934'))
#print(adress.show_all_contacts())
