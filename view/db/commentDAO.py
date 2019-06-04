import pymongo

class Comment():
    def __init__(self,db):
        self.comments = pymongo.collection.Collection(db,'Comment')
            
    def adminValidation(self,commentDict):
        #아이디 비밀번호가 입력 되었는지 확인 후 true반환
        if self.comments.find_one(commentDict):
            return False
        else:
            return True

    def commentAuthentication(self,commentDict):
        if self.comments.find_one(commentDict):
            return True
        else:
            return False

    def commentCreate(self,commentDict):
        try:
            self.comments.insert_one(commentDict)
            return True
        except:
            return False

    def getAllComments(self, ProjIdx):
        try:
            result = self.comments.find({"projIdx": {"$eq": ProjIdx}})
            return result
        except:
            return False
#삭제권한

