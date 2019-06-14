import pymongo
from bson.objectid import ObjectId

class Comment():
    def __init__(self,db):
        self.comments = pymongo.collection.Collection(db,'Comment')
    
#    def deleteAuth(self, commentUser):
#        try:
#            return
#        except:
#            return
    
    
    def commentCreate(self,commentDict):
        try:
            commentDict["proj_id"] = ObjectId(commentDict["proj_id"])
            result = self.comments.insert_one(commentDict)
            return result
        except:
            return False

    def getAllComments(self, ProjIdx):
        try:
            result = self.comments.find({"proj_id": ObjectId(ProjIdx)})
            return result
        except:
            return False

    def likeComments(self, commentsId):
        try:
            result = self.comments.update({"_id": ObjectId(commentsId)},{ "$inc": {"like":+1}})
            return result
        except:
            return False

    def deleteComments(self, commentsId):
        try:
            result = self.comments.delete_one({"_id": ObjectId(commentsId)})
            return result
        except:
            return False
