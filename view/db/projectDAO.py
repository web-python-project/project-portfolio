import pymongo

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
