# -*- coding:utf-8 -*-

class NotIdentifiedError(Exception):
    def __init__(self, error_type):
        self.error_type = error_type

    def __str__(self):
        msg = "{} not Indentifield,you must declare it ".format(self.error_type)
        return msg
