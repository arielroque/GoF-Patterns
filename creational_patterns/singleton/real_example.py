import sqlite3

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if (cls not in cls._instances):
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if (self.connection == None):
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Object created:",db1)
print("Object created:",db2)



