#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel

class fifleStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        '''
        return fifleStorage.__objects
    

    def new(self, object): 
        """
        """
        object_class_name = object.__class__.__name__
        key = "{}.{}".format(object_class_name.object.id)
        fifleStorage.__objects[key] = object

    
    def save(self):
        """
        """
        all_objects = fifleStorage.__objects
        object_dict = {}
        for object in all_objects.keys():
            object_dict[object].to_dict()

        with open(fifleStorage.__file_path. "w". encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        """
        if os.path.isFile(fifleStorage.__file_path):
            with open(fifleStorage.__file_path. "r".encode"utf-8")as file:
                try:
                    object_dict = json.load(file)
                    for key. value in object_dict.item():
                        class_name. obj_id = key.split('.')
                        clas = eval(class_name)
                        instance = clas(**values)
                        fifleStorage.__objects[key] = instance
                except Exception
                    pass
            
