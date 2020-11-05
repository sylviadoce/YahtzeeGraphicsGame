#
# Sylvia Chin
#
# Keeps track of points for each score cell based on the dice's hand
#
from graphics import *
from Button import Button 
from Die import Die 

class ScoreCell:
    
    """A score cell is a labeled rectangle in a window. It evaluates
    the chosen category and defines each hand so the points will display.
    The different hands each have a method: onesValues() to sum ones,
    twosValues() to sum twos, threeValues() to sum threes, foursValues()
    to sum fours, fivesValues() to sum fives, sixesValues() to sum sixes,
    threeOfAKind() to detect three same values, fourOfAKind() to detect four
    same values, fullHouse() to detect a pair and triplet, smallStraight()
    to detect four consecutive values, largeStraight() to detect five
    consecutive values, chance() to sum all values, and
    yahtzeeFiveOfAKind() to detect five same values."""
    
    def __init__(self, win, center, width, height, label):
        "Creates a rectangular score cell."

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
        self.label.draw(win)
    
    def onesValues(self, val1, val2, val3, val4, val5):
        "Totals all of the ones rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0

        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
                # Multiply the value of ones by ones and set that as
                    # as the total to be accessed
                total = ones*1
            elif i == 2:
                twos = twos + 1
            elif i == 3:
                threes = threes + 1
            elif i == 4:
                fours = fours + 1
            elif i == 5:
                fives = fives + 1
            elif i == 6:
                sixes = sixes + 1

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def twosValues(self, val1, val2, val3, val4, val5):
        "Totals all of the twos rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0

        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            elif i == 2:
                twos = twos + 1
                total = twos*2
            elif i == 3:
                threes = threes + 1
            elif i == 4:
                fours = fours + 1
            elif i == 5:
                fives = fives + 1
            elif i == 6:
                sixes = sixes + 1

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def threesValues(self, val1, val2, val3, val4, val5):
        "Totals all of the threes rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0


        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            elif i == 2:
                twos = twos + 1
            elif i == 3:
                threes = threes + 1
                total = threes*3
            elif i == 4:
                fours = fours + 1
            elif i == 5:
                fives = fives + 1
            elif i == 6:
                sixes = sixes + 1

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def foursValues(self, val1, val2, val3, val4, val5):
        "Totals all of the fours rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0

        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            elif i == 2:
                twos = twos + 1
            elif i == 3:
                threes = threes + 1
            elif i == 4:
                fours = fours + 1
                total = fours*4
            elif i == 5:
                fives = fives + 1
            elif i == 6:
                sixes = sixes + 1

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def fivesValues(self, val1, val2, val3, val4, val5):
        "Totals all of the fives rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0

        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            elif i == 2:
                twos = twos + 1
            elif i == 3:
                threes = threes + 1
            elif i == 4:
                fours = fours + 1
            elif i == 5:
                fives = fives + 1
                total = fives*5
            elif i == 6:
                sixes = sixes + 1

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def sixesValues(self, val1, val2, val3, val4, val5):
        "Totals all of the sixes rolled and displays score."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0

        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            elif i == 2:
                twos = twos + 1
            elif i == 3:
                threes = threes + 1
            elif i == 4:
                fours = fours + 1
            elif i == 5:
                fives = fives + 1
            elif i == 6:
                sixes = sixes + 1
                total = sixes*6

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def threeOfAKind(self, val1, val2, val3, val4, val5):
        """Totals all of the dice rolled if there are three same values
        and displays score."""

        # Create a variable 'total' to count points to be displayed
        total = 0

        # Check all three-dice permutations, include four-dice permutations
        if (val1 == val2 == val3 or val1 == val2 == val4 or val1 == val2
            == val5 or val1 == val3 == val4 or val1 == val3 == val5 or
            val1 == val4 == val5 or val2 == val3 == val4 or val2 == val3
            == val5 or val2 == val4 == val5 or val3 == val4 == val5 or
            val1 == val2 == val3 == val4 or val1 == val2 == val4 == val5
            or val1 == val2 == val3 == val5 or val1 == val3 == val4 ==
            val5 or val2 == val3 == val4 == val5 or val1 == val2 == val3
            == val4 == val5):
            # If there is one combination of three same values, the total
                # is the sum of all dice values
            total = val1+val2+val3+val4+val5
        # If not, the total is 0
        else:
            total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def fourOfAKind(self, val1, val2, val3, val4, val5):
        """Totals all of the dice rolled if there are four same values
        and displays score."""

        # Create a variable 'total' to count points to be displayed
        total = 0

        # Check all four-dice permutations
        if (val1 == val2 == val3 == val4 or val1 == val2 == val4 == val5
            or val1 == val2 == val3 == val5 or val1 == val3 == val4 ==
            val5 or val2 == val3 == val4 == val5 or val1 == val2 == val3
            == val4 == val5):
            # If there is one combination of four same values, the total
                # is the sum of all dice values
            total = val1+val2+val3+val4+val5
        # If not, the total is 0
        else:
            total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)
            
    def fullHouse(self, val1, val2, val3, val4, val5):
        "Total is 25 if there is a two pair and a three of a kind."

        # Create a variable 'total' to count points to be displayed
        total = 0
        # Check 3 of a kind and return 3 same and then check last 2 are equal
            # If so, 25 points, otherwise 0 points
        if (val1 == val2 == val3):
            if val4 == val5:
                total = 25
            else:
                total = 0
        elif (val1 == val2 == val4):
            if val3 == val5:
                total = 25
            else:
                total = 0
        elif (val1 == val2 == val5):
            if val3 == val4:
                total = 25
            else:
                total = 0
        elif (val1 == val3 == val4):
            if val2 == val5:
                total = 25
            else:
                total = 0
        elif (val1 == val3 == val5):
            if val2 == val4:
                total = 25
            else:
                total = 0
        elif (val1 == val4 == val5):
            if val2 == val3:
                total = 25
            else:
                total = 0
        elif (val2 == val3 == val4):
            if val1 == val5:
                total = 25
            else:
                total = 0
        elif (val2 == val3 == val5):
            if val1 == val4:
                total = 25
            else:
                total = 0
        elif (val2 == val4 == val5):
            if val1 == val3:
                total = 25
            else:
                total = 0
        elif (val3 == val4 == val5):
            if val1 == val2:
                total = 25
            else:
                total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def smallStraight(self, val1, val2, val3, val4, val5):
        "Total is 30 if there are four consecutive dice."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        
        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            if i == 2:
                twos = twos + 1
            if i == 3:
                threes = threes + 1
            if i == 4:
                fours = fours + 1
            if i == 5:
                fives = fives + 1
            if i == 6:
                sixes = sixes + 1

        # If there are at least one of each number 1-4 or 2-5 or 3-6, there 
            # is a straight
        # Otherwise, the total is 0
        if ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1:
            total = 30
        elif twos >= 1 and threes >= 1 and fours >= 1 and fives >=1:
            total = 30
        elif threes >= 1 and fours >= 1 and fives >= 1 and sixes >= 1:
            total = 30
        elif (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1 and
              fives >= 1):
            total = 30
        elif (twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1 and
              sixes >= 1):
            total = 30
        else:
            total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def largeStraight(self, val1, val2, val3, val4, val5):
        "Total is 40 if there are five consecutive dice."
        
        # Create a variable 'total' to count points to be displayed
        total = 0
        # Create a variable to count each die value 1-6
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        
        # Go through each die value using a for loop to check for
            # its value and keep track of it
        for i in (val1, val2, val3, val4, val5):
            if i == 1:
                ones = ones + 1
            if i == 2:
                twos = twos + 1
            if i == 3:
                threes = threes + 1
            if i == 4:
                fours = fours + 1
            if i == 5:
                fives = fives + 1
            if i == 6:
                sixes = sixes + 1

        # If there are at least one of each number 1-5 or 2-6, there is a  
            # straight
        # Otherwise, the total is 0
        if (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1 and
            fives >= 1):
            total = 40
        elif (twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1
              and sixes >= 1):
            total = 40
        else:
            total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)

    def chance(self, val1, val2, val3, val4, val5):
        "Total all dice values."

        # Create a variable 'total' to count points to be displayed
        total = 0
        # The total is always just the sum of each value
        total = val1+val2+val3+val4+val5

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)
        
    def yahtzeeFiveOfAKind(self, val1, val2, val3, val4, val5):
        "Total is 50 if there are five same values."

        # Create a variable 'total' to count points to be displayed
        total = 0

        # Check if all five values are the same
        if (val1 == val2 == val3 == val4 == val5):
            # If so, the value is 50
            total = 50
        # If not, the value is 0
        else:
            total = 0

        # Get total and set the label as the new value
        self.value = total
        self.label.setText(self.value)
        
    def getScore(self):
        """Returns the score string of the round from die based on
        its category."""
        return self.value

    
        


    
    
        
    
