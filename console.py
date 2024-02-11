#!/usr/bin/python3

import  cmd
import shlex
from models.base_model import BaseModel
from models import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["Basemodel"]

    def do_quit(self, args):
        """
        """
        return True
    
    def do_EOF(self, args):
        """
        """
        return True
    
    def do_emptyline(self, args):
        """
        """
        pass

    def do_create(self, args):
        """
        """
        _cmd = shlex.split(args)

        if len(_cmd) == 0:
            print("** class name missing**")
        elif _cmd[0] not in self.valid_classes:
            print("**class doesn't exist**")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_update(self, args):
        """
        """
        _cmd = shlex.split(args)

        if len(_cmd) == 0:
            print("**class dosen't exist**")
        elif len(_cmd) < 2:
            print("**instance id missing**")
        else:
            objects  = FileStorage.all()
            key = "{}.{}".format(_cmd[0], _cmd[1])
            if key not in object:
                print("**no instance found**")
            elif len(_cmd) < 3: 
                print("**attribute name missing")
            elif len(_cmd) < 4:
                print("**value missing**")
            else:
                obj = objects[key]

                attr_name = _cmd[2]
                attr_value = _cmd[1]

                try:
                    attr_value = eval(attr_value)
                except Exception as e:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
   

    def do_show(self, args):
        _cmd = shlex.split(args)
        objects = FileStorage.all()
        if len(_cmd) == 0:
            print("**class name missing**")
        elif _cmd[0] not in self.valid_classes:
            print("**doesn't exist**")
        elif len(_cmd) == 1:
            print("**instance id missing**")
        elif "{}.{}".format(_cmd[0], _cmd[1]) not in objects:
            print("**no instance found**")
        else:
            print(objects["{}.{}".format(_cmd[0], _cmd[1])])

    def do_destroy(self, args):
        """
        """
        _cmd = shlex.split(args)
        objects = FileStorage.all()
        if len(_cmd) == 0:
            print("**class name missing**")
        elif _cmd[0] not in self.valid_classes:
            print("**class dosen't exist**")
        elif len(_cmd) == 0:
            print("**instance id missing**")
        elif "{}.{}".format(args[0], args[1]) not in object.key():
            print("**no isinstance fund**")
        else:
            del object["{}.{}".format(args[0], args[1])]
            FileStorage.save()
    
    def do_all(self, args):
        """
        """
        _cmd = shlex.split(args)
        objects = FileStorage.all()

        if len(_cmd) == 0:
            for key, value in objects.items():
                print(str(value))
        elif _cmd[0] not in self.valid_classes:
            print("**class dosen't exist**")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == _cmd[0]:
                  print(str(value))

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
