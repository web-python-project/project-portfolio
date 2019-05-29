import pymongo

class User():
    def __init__(self,db):
        self.users = pymongo.collection.Collection(db,'Users')
    
    def userValidation(self, userDict):
        if self.users.find_one(userDict):
            return False
        else:
            return True

def userAuthentication(self,userDict):
    if self.users.find_one(userDict):
        return True
    else:
        return False

def userCreate(self,userDict):
    if self.userValidation({"userEmail":userDict["userEmail"]}):
        try:
            self.users.insert_one(userDict)
            return True
        except:
            return False
    else:
        return False
