import pymongo
from bson.objectid import ObjectId

class Project():
    def __init__(self,db):
        self.projects = pymongo.collection.Collection(db,'Project')
    
    def userValidation(self, projectDict):
        if self.projects.find_one(projectDict):
            return False
        else:
            return True

    def getAllProject(self):
        try:
            result = self.projects.find({})
            return result
        except:
            return False

    def getOneProject(self,index):
        try:
            result = self.projects.find({"_id": ObjectId(index)})
            return result
        except:
            return False

    def deleteProject(self,projectId):
        try:
            result = self.projects.delete_one({"_id": ObjectId(projectId["_id"])})
            return result
        except:
            return False
