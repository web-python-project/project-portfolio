import pymongo
from bson.objectid import ObjectId

class Comment():
    def __init__(self,db):
        self.comments = pymongo.collection.Collection(db,'Comment')
    
    #삭제권한
#    def deleteAuth(self, commentUser):
#        userInfo = self.comments.find({"_id": ObjectId(commentUser["_id"])},{"commentEmail": commentUser["commentEmail"]})
##        return commentUser["commentPassword"]
#        if userInfo["commentPassword"] == commentUser["commentPassword"]:
#            return True
#        else:
#            return False


    def commentCreate(self,commentDict):
        try:
            commentDict["proj_id"] = ObjectId(commentDict["proj_id"])
            commentDict["like"]= int(commentDict["like"])
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
        #result = commentsId
        try:
            result = self.comments.delete_one({"_id": ObjectId(commentsId["_id"])})
            return True
        except:
            return False



#    def deleteComments(self, commentsId):
#        #result = commentsId
#        result = self.deleteAuth(commentsId)
#        return result
##        if self.deleteAuth(commentsId):
##            try:
##                result = self.comments.delete_one({"_id": ObjectId(commentsId["_id"])})
##                return True
##            except:
##                return False
##        else:
##            return False

