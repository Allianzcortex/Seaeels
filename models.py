
class BaseModels(object):
    """
    use the model to describe the basic model
    """
    @classmethod
    def save(cls,**kwargs):
        for k,v in kwargs.items():
            setattr(cls,k,v)