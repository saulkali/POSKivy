import os 

def singleton(cls):
    instances = dict()
    def wrap(*args,**kargs):
        if cls in instances:
            return instances[cls]
        new_intance = cls(*args,**kargs)
        instances[cls] = new_intance
        return instances[cls]
    return wrap

def getFile(file):
    dirname = os.path.dirname(__file__)+"/"+file
    print("dirname: ",dirname)
    return dirname


