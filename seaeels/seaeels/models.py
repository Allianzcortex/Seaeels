class BaseModels(object):
    """
    use the model to describe the basic model
    """

    @classmethod
    def save(cls):
        cls.item_list = []
        for item in dir(cls):
            if not item.startswith('__') and item is not 'save':
                cls.item_list.append(item)