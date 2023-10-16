from ContactBook import ContactBook

class ContactBookController:
    
    ''' basic responsibility of a ContactBookController object is to carry out the various use cases:
        1. Insertion of a new Contact
        2. Deletion of an existing Contact
        3. Update an existing Contact
        4. Display all Contacts
        5. Search for an existing Contact '''
    
    def __init__(self):
        self.cb_obj = ContactBook()

    def add_new_contact(self):
        print("CONTACT INSERTION GOING ON ...", end='\n\n')
        print("Enter full name: ", end= " ")
        name = input()

        is_found = self.cb_obj.search_contact(name)

        if is_found == 1:
            print("\nContact already exists in Contact Book!\n")
        else:
             print("Enter phone number: ", end=" ")
             phone= input()
             print("Enter email address: ", end=" ")
             email = input()
             print("Enter address: ", end=" ")
             address = input()
             print("Enter ZIP: ", end=" ")
             zip = input()
             self.cb_obj.add_contact(name.title(), phone, email, address, zip)
    

    def delete_existing_contact(self):
        print("\nEnter contact name you would like to delete (make sure to capitalise first letter of first, last & middle name): ")
        to_be_del_contact = input()

        self.cb_obj.delete_contact(to_be_del_contact)
    
    def update_existing_contact(self):
        print("\nEnter contact name that you would like to update (make sure to capitalise first letter of first, last & middle name): ", end=" ")
        edit_contact = input()

        is_found = self.cb_obj.search_contact(edit_contact)

        if is_found == 0:
            print("\nContact could not be found in Contact Book!", end='\n\n')
        else:
            print("\n1. Phone Number  2. Email Address   3. Address   4. ZIP")
            print("Select the number corresponding to the attribute you would like to edit:", end = " ")
            attr_num = int(input())
            print("\nPlease mention the edited value:", end=" ")
            edit_value = input()
            self.cb_obj.update_contact(edit_contact, attr_num, edit_value)
    
    def search_contact(self):
        print("\nEnter the contact you would like to search for (make sure to capitalise first letter of first, last & middle name): ", end= " ")
        to_search = input()

        is_found = self.cb_obj.search_contact(to_search)
        if is_found == 1:
            print("\nContact has been searched successfully!\n")
        else: 
            print("\nCould not find contact! Try again!\n")
    
    def display_all_contacts(self):
        print("\nCOMPLETE LIST OF CONTACTS IN THE CONTACT BOOK:\n")
        self.cb_obj.display_all_contacts()









