

#abstract toolkit
#all toolkits must have the same interface


def renderer(): raise NotImplementedError

from abstract_toolkit import *


# abstract interface for event
class Event:

    def getKeyCode(self):
        "return ascii code of the key being pressed"
        raise NotImplementedError
        

