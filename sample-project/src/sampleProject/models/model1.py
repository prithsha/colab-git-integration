from sampleProject.utility import myUtility
from sampleProject.common import constant



class ModelOne(object):
    """docstring for ModelOne."""
    def __init__(self):
        super(ModelOne, self).__init__()

        self.number = 50

    def get_number(self):
        return self.number
    
    def get_version(self):
        return myUtility.get_random_number() + constant.VERSION

    
    