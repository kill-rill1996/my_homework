import time
from reuserpatterns.singletones import SingletoneByName


# Заметка, можно применить стратегию если добавить стратегию логирования
class Logger(metaclass=SingletoneByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)


# декоратор
def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG------->', func.__name__, end - start)
        return result
    return inner

