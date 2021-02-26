import time
from reuserpatterns.singletones import SingletoneByName


class Logger(metaclass=SingletoneByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)
