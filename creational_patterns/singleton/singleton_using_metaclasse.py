class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

l1 = Logger()
l2 = Logger()

print("Object created:",l1)
print("Object created:",l2)