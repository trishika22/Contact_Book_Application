![image](https://github.com/trishika22/Contact_Book_Application/assets/81105231/4ad66534-f50b-46d0-86a2-491347ce67a8)![image](https://github.com/trishika22/Contact_Book_Application/assets/81105231/819c4ea0-c8fe-4378-8ac2-9ad4c3a6e517)# Contact Book Application
This is a simple command line based contact book application in Python programming language. 

A contact book holds a collection of contacts, where every contact will store the following information about a person: Name, Phone Number, Email, Address and ZIP. This program can perform (1) insertion of a new contact (2) deletion of an existing contact (3) update on an existing contact (4) search for an existing contact (5) display all contacts present in the contact book.

Please find below the designated responsibilities of the underlying classes & their associated methods that make up the Contact Book Application:

**class Person**
  An object of this class maintains the information of a single individual in a Contact Book.
  
	Constructor
	def __init__(self, phone, email, address, zip)
		
		Parameters
		phone- the person's phone number
		email- the person's email address
		address- the person's address
		zip- the person's address' ZIP
	
	Methods
	def get_phone(self)
		Accessor for the person's phone number
		Returns:
			the person's phone number
	
	def set_phone(self,phone)
		Setter for the person's phone number
		Returns:
			None
	
	def get_email(self)
		Accessor for the person's email address
		Returns:
			the person's email address
	
	def set_email(self,email)
		Setter for the person's email address
		Returns:
			None
	
	def get_address(self)
		Accessor for the person's address
		Returns:
			the person's address
	
	def set_address(self,address)
		Setter for the person's address
		Returns:
			None
	
	def get_zip(self)
		Accessor for the person's address' ZIP
		Returns:
			the person's address' ZIP
	
	def set_zip(self,zip)
		Setter for the person's address' ZIP
		Returns:
			None



**class Contact**
	An object of this class maintains the information of a single contact in a Contact Book.
	
	Constructor
	def __init__(self)
		
		Parameters
		contact_name- the person's full name
		p_obj- Person class object
	
	Methods
	def get_contact_name(self)
		Accessor for the person's full name
		Returns:
			the person's full name
	
	def set_contact_name(self,contact_name)
		Setter for the person's full name
		Returns:
			None
	
	def get_person(self)
		Accessor for the Person class object
		Returns:
			the person's email address, phone number, email address, address & ZIP
	
	def set_person(self, email, phone, address, zip)
		Setter for the Person class object
		Returns:
			None
		
**class ContactBook**
	An object of this class maintains the information of all the contacts present in the ContactBook and assists in loading the data to the file system (aka pickle file)

	Constructor
	def __init__(self)
	
		Parameters
		c_obj- object of the Contact class
		fs_obj- object of the FileSystem class
	
	Methods
	def add_contact(self, name, phone, email, address, zip)
		Set the values for the Contact class object and add the same object in the file system
		Returns:
			None
	
	def delete_contact(self, to_be_del_contact)
		Load the existing database, scan for the contact to be deleted and remove its entry from the file system. If contact not found, deletion operation is not performed.
		Returns:
			None
	
	def update_contact(self, edit_contact, attr_num, edit_value)
		Load the existing database to scan for the contact to be edited and perform the edit based on the attribute passes. If contact not found, update operation is not performed. Please note that the contact_name attribute cannot be alerted.
	
	def search_contact(self, to_search):
		Load the existing database and search for the contact requested. If found, return 1, else, return 0
		Returns:
			found
	
	def display_all_contacts(self)
		Load the exisitng database and display all the contacts present in the file system. If no contacts are found, display "Contact book is empty!" message
		Returns:
			None
			
**class FileSystem**
	An object of this class is responsible to load and unload data from the file system/ database/ pickle file
	
	Constructor
	def __init__(self)
	
		Parameters
		db - dictionary responsible to store data in the form of 'contact_name': [phone number, email address, address, zip
		dbfile - pickle file where all the contacts are saved
			
	Methods
	def store_data(self, c_obj)
		Stores a single contact entry into the database
		Returns:
			None
			
	def store_database(self, database)
		Stores all contacts into the database
		
	def load_data(self)
		Stores all the contacts present in the file system into a dictionary
		Returns:
		db- dictionary meant to store all contacts present in database
		

**Class ContactBookController**
	The basic responsibility of an AddressBookController object is to carry out the various use cases. 
	
	Constructor
	def __init__(self)
	
		Parameters
		cb_obj- object of ContactBook class
	
	Methods
	def add_new_contact(self)
		Allow the user to perform the Add a Contact Use Case
	
	def delete_existing_contact(self)
		Allow the user to perform the Delete a Contact Use Case
	
	def update_existing_contact(self)
		Allow the user to perform the Update a Contact Use Case
	
	def search_contact(self)
		Allow the user to perform the Search a Contact Use Case
	
	def display_all_contacts(self)
		Allow the user to perform the Display all Contacts Use Case
	
**Class ContactBookApplication**
	Main class for the application that triggers the creation of the ContactBook & ContactBookController class objects 
	
	Methods
	def print_choices(self)
		Prints the list of available operations that can be performed by the ContactBookApplication 
	
	def select_choice(self)
		Make a choice of the operation to perform, to invoke its corresponding method





