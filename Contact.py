from Person import Person

class Contact:
    
    ''' maintains the information of a single contact in a Contact Book '''

    def __init__(self):
        self.contact_name = ""
        self.p_obj = Person("", "", "", "")
    
    def get_contact_name(self):
        return self.contact_name
    
    def set_contact_name(self, contact_name):
        self.contact_name = contact_name
    
    def get_person(self):
        return self.p_obj.get_phone(), self.p_obj.get_email(), self.p_obj.get_address(), self.p_obj.get_zip()
    
    def set_person(self, email, phone, address, zip):
        self.p_obj.set_email(email)
        self.p_obj.set_phone(phone)
        self.p_obj.set_address(address)
        self.p_obj.set_zip(zip)

    

