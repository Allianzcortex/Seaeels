# -*- coding:utf-8 -*-

"""
The BaseSite should be the base class for the all Site Model
"""

class BaseSite(object):
    def __init__(self, name, model):

        self.name = name
        self.item_list = {}
        for item in dir(model):
            if not item.startswith('__') and item is not 'save':
                self.item_list[item] = getattr(model, item)
        self.result_list = {}

    def __str__(self):
        return 'BaseSite {}'.format(self.name)