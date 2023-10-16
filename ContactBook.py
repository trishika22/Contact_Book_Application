from FileSystem import FileSystem
from Contact import Contact
from tabulate import tabulate

class ContactBook:

    ''' maintains the information of all the contacts present in the ContactBook and assists in loading the data to the file system (aka pickle file) '''
    
    def __init__(self):
        self.c_obj = Contact()
        self.fs_obj = FileSystem()


    def add_contact(self, name, phone, email, address, zip):
        self.c_obj.set_contact_name(name)
        self.c_obj.set_person(phone, email, address, zip)
        self.fs_obj.store_data(self.c_obj)

        print("\nThe following contact has successfully been added: ")
        print(tabulate([[name, phone, email, address, zip]], headers= ['Full Name', 'Phone Number', 'Email', 'Address', 'ZIP']), end='\n\n')

    
    def delete_contact(self, to_be_del_contact):
        temp_db = self.fs_obj.load_data()
        found = 0

        for contact in list(temp_db.keys()):
            if to_be_del_contact == contact:
                del temp_db[to_be_del_contact]
                self.fs_obj.store_database(temp_db)
                found = 1
                print("\nContact has successfully been deleted!", end='\n\n')

        if found == 0:
            print("\nContact not found! Please try again!", end='\n\n')


    def update_contact(self, edit_contact, attr_num, edit_value):
        temp_db = self.fs_obj.load_data()
        found = 0

        for contact in list(temp_db.keys()):
            if edit_contact == contact:
                temp_db[edit_contact][attr_num - 1] = edit_value
                self.fs_obj.store_database(temp_db)
                found = 1
                print("\nContact has successfully been edited!")
                print(tabulate([[edit_contact, temp_db[edit_contact][0], temp_db[edit_contact][1], temp_db[edit_contact][2], temp_db[edit_contact][3]]], headers= ['Full Name', 'Phone Number', 'Email', 'Address', 'ZIP']), end='\n\n')

        if found == 0:
            print("Contact not found! Please try again!", end='\n\n')

    
    def search_contact(self, to_search):
        temp_db = self.fs_obj.load_data()
        found = 0

        for contact in list(temp_db.keys()):
            if to_search == contact:
                print('\n')
                print(tabulate([[to_search, temp_db[to_search][0], temp_db[to_search][1], temp_db[to_search][2], temp_db[to_search][3]]], headers= ['Full Name', 'Phone Number', 'Email', 'Address', 'ZIP']), end='\n')
                found = 1

        return found
    

    def display_all_contacts(self):
        data = self.fs_obj.load_data()
        if len(data) == 0:
            print("Contact book is empty!", end='\n\n')
        else:
            data = [[key] + val for key, val in self.fs_obj.load_data().items()]
            print(tabulate(data, headers= ['Full Name', 'Phone Number', 'Email', 'Address', 'ZIP']), end='\n\n')
    
    