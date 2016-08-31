import requests
from bs4 import BeautifulSoup
from unittest import *


class Unittest(unitest.main):
    def loadup(self):
        pass


class Factorial(object):
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = self.__call__(n - 1)
        return self.cache[n]


if __name__ == '__main__':
    run()
