import pymongo

from bson.objectid import ObjectId



"""MongoDB Database Access Object"""

class Posts():

   

   def __init__(self,db):

      self.projects = pymongo.collection.Collection(db,'Project')



   def postCreate(self,projectDict):

      try:

         obj_id = self.projects.insert_one(projectDict).inserted_id

         return obj_id

      except:

         return False



   def postDelete(self,obj_id):

      try:

         self.projects.delete_one({"_id":ObjectId(obj_id)})

         return True

      except:

         return False



   def postUpdate(self,projectDict):

      #try:

      self.projects.find_and_modify(

         {"_id": ObjectId(projectDict["obj_id"])},

         {"$set":{"title":projectDict["title"],"description":projectDict["description"]}},

         upsert=False

         )

      return True

      #except:

      #   return False



   def getAllposts(self):

      try:

         result = self.projects.find({})

         return result

      except:

         return False

