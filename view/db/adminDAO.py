import pymongo

class Admin():
    def __init__(self,db):
        self.admin0 = pymongo.collection.Collection(db,'Admin')
    
    def adminValidation(self, adminDict):
        if self.admin0.find_one(adminDict):
            return False
        else:
            return True

    def adminAuthentication(self,adminDict):
        if self.admin0.find_one(adminDict):
            return True
        else:
            return False
