class Rectangle:

    def __init__(self, x, y, h, w):
        '''
        Defines instance variables and sets values to 0 if parameters are less than 0
        args: x y coordinates, height and width of Rectangle
        return: None
        '''

        self.x = x
        self.y = y
        self.height = h
        self.width = w

        if x < 0:
            self.x = 0
        if y < 0:
            self.y = 0
        if h < 0:
            self.height = 0
        if w < 0:
            self.width = 0

    def __str__(self):
        '''
        returns string giving x y coordinates, height, and width
        args: none
        return: string w/ data
        '''
        
        return f'(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}'