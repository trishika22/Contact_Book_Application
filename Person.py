class Person:
    
    ''' maintains the information of a single individual in a Contact Book '''

    def __init__(self, phone, email, address, zip):
        self.phone = phone
        self.email = email
        self.address = address
        self.zip = zip
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self,phone):
        self.phone = phone
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address

    def get_zip(self):
        return self.zip
    
    def set_zip(self, zip):
        self.zip = zip


    

 




