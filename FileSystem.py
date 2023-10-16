import pickle

class FileSystem:
    '''  responsible to load and unload data from the file system/ database/ pickle file '''

    def __init__(self):
        self.db = {}  
        dbfile = open('contactBookPickle.pkl', 'ab')
        pickle.dump(self.db, dbfile)
        dbfile.close()      
        
    def store_data(self, c_obj):
        self.db[c_obj.contact_name] = [c_obj.p_obj.phone, c_obj.p_obj.email, c_obj.p_obj.address, c_obj.p_obj.zip]
        dbfile = open('contactBookPickle.pkl', 'ab')
        pickle.dump(self.db, dbfile)
        dbfile.close()

    
    def store_database(self, database):
        dbfile = open('contactBookPickle.pkl', 'wb')
        pickle.dump(database, dbfile)
        dbfile.close()

    
    def load_data(self):
        dbfile = open('contactBookPickle.pkl', 'rb')

        try:
            while True:
                all_data = pickle.load(dbfile)
                self.db.update(all_data)
        except EOFError:
            pass
        
        return self.db

