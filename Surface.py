from Rectangle import Rectangle

class Surface:

    def __init__(self, filename, x, y, h, w):
        '''
        Defines instance variables rect and myimage
        args: filename, x and y coordinates, and rectangle height and width
        return: None
        '''
        
        self.rect = Rectangle(x, y, h, w)
        self.image = str(filename)

    def getRect(self):
        '''
        Gets and returns rectangle from __init__
        args: none
        return: rectangle
        '''
        return self.rect