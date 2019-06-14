import pymongo

class User():
    def __init__(self,db):
        self.users = pymongo.collection.Collection(db,'Users')

    #회원가입시) db에 동일한 아이디가 있는지 확인. 있으면 false=> 가입불가눙
    def userValidation(self, userDict):
        if self.users.find_one(userDict):
            return False
        else:
            return True

    #로그인시) db에 동일한 아이디 있는지 확인.
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
