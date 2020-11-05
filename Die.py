#
# Sylvia Chin
#
# Die class module - drawing itself, rolling a 6-sided die
#
from random import randrange
from graphics import *

class Die:

    """A die is a square (rectangle) that generates random values,
    displayed by an integer inside on the die face. It can be rolled,
    giving a new value, with the roll() method."""

    def __init__(self, win, center, width, height, sides, label):
        "Creates a rectangular die."
        # Use 6-sided die only by setting the number of sides to 6
        self.sides = 6

        # Define what center means using the width and height
            # dimensions
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.setSize(20)
        self.label.draw(win)

    def roll(self):
        "Assigns the die's value to a random integer from 1 to 6."
        # Use the imported randrange function to get a random integer
        self.value = randrange(1,7)
        # Assign the new value to the die's label
        self.label.setText(self.value)    

    def getValue(self):
        "Returns the value of the die."
        return self.value

    
