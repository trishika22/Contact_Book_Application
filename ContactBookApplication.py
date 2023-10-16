from ContactBookController import ContactBookController

class ContactBookApplication:

    ''' main class for the application that triggers the creation of the ContactBook & ContactBookController class objects '''

    def print_choices(self):
        print("*** SilverVista's Contact Book Application ***", end='\n\n')
        print("Select any of the listed operations (1-5):", end='\n\n')
        print("1. Add New Contact")
        print("2. Delete Existing Contact")
        print("3. Update Existing Contact")
        print("4. Display All Contacts")
        print("5. Search for a particular Contact")
        print("6. Exit program", end='\n\n')
        
    def select_choice(self):
        self.print_choices()
        cbc_obj = ContactBookController()

        while(1):
            print("Your choice: ", end=" ")
            try:
                choice = int(input())
            except ValueError:
                print("Please enter a valid choice to proceed.")
                print("\n... LEAVING CONTACT BOOK APPLICATION")
                break

            match choice:
                case 1: cbc_obj.add_new_contact()
                case 2: cbc_obj.delete_existing_contact()
                case 3: cbc_obj.update_existing_contact()
                case 4: cbc_obj.display_all_contacts()
                case 5: cbc_obj.search_contact()
                case 6: print("\n... LEAVING CONTACT BOOK APPLICATION"); exit()
                case _: print("Invalid choice! Please try again")

            self.print_choices()
            
            



        
