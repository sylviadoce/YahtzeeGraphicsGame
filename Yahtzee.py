#
# Sylvia Chin
#
# One-player game of Yahtzee using Button, Die, and ScoreCell classes
#
from graphics import *
from Button import Button
from Die import Die
from ScoreCell import ScoreCell

def main():

    # Create a small graphics window for player name
    namewin = GraphWin("Yahtzee Player Name", 200, 350)

    # Instruct the user to enter their name in the entry box
    t = Text(Point(100, 80), "Please enter your name:")
    t.draw(namewin)
    # Create and draw the entry box
    tinput = Entry(Point(100, 100), 20)
    tinput.draw(namewin)

    # Create a 'Start' button
    startbutton = Button(namewin, Point(100,300), 40, 15, "Start")
    # Activate the button
    startbutton.activate()

    # Detect when the 'Start' button is clicked using while it isn't clicked
        # Also serves as the pause for the entry box input
    pt = namewin.getMouse() 
    while not startbutton.clicked(pt):
        pt = namewin.getMouse()

    # Save user's name input into a variable and convert to a string            
    tname = str(tinput.getText())

    # Check if the name's string value is empty
        # If it's empty, close the window and re-run the program
        # If there IS something in the entry box, close the name window and go
        # onto the Yahtzee program (open the Yahtzee window)
    if not tname:
        namewin.close()
        main()
    else:
        namewin.close()
        win = GraphWin("Yahtzee 1-Player Game", 700, 900)

    # Display the player name as text and draw in the window
    playername = Text(Point(350, 40), str(tname))
    playername.draw(win)

    # Display number of games played
    numgames = Text(Point(590,25), "Number of Games Played: ")
    numgames.draw(win)
    # Keep track of number of games with variable 'games'
    games = 0
    # Display high score
    highscore = Text(Point(626,45), "High Score: ")
    highscore.draw(win)
    # Keep track of high score with variable 'newhighscore'
    newhighscore = 0

    # Create an instructions message box and label in the window 
    instructionsbox = Rectangle(Point(60,260), Point(640,220))
    instructionsbox.draw(win)
    instructionslabel = Text(Point(350,200), "Instructions")
    instructionslabel.draw(win)
    instructions = Text(Point(350, 240), "Click the Roll button to begin.")
    instructions.draw(win)

    # Create labels for score cell and each category
    Text(Point(350, 290), "Score Chart").draw(win)
    Text(Point(190,325), "ONES").draw(win)
    Text(Point(190,370), "TWOS").draw(win)
    Text(Point(180,415), "THREES").draw(win)
    Text(Point(185,460), "FOURS").draw(win)
    Text(Point(185,505), "FIVES").draw(win)
    Text(Point(185,550), "SIXES").draw(win)
    Text(Point(185,595), "SUM").draw(win)
    Text(Point(185,640), "BONUS").draw(win)
    Text(Point(420,325), "THREE OF A KIND").draw(win)
    Text(Point(420,370), "FOUR OF A KIND").draw(win)
    Text(Point(430,415), "FULL HOUSE").draw(win)
    Text(Point(425,460), "SMALL STRAIGHT").draw(win)
    Text(Point(425,505), "LARGE STRAIGHT").draw(win)
    Text(Point(445,550), "CHANCE").draw(win)
    Text(Point(440,595), "YAHTZEE").draw(win)
    Text(Point(440,640), "TOTAL SCORE").draw(win)
    
    # Create a quit button in the top left corner that closes win when 
        # clicked from Button class
    quitbutton = Button(win, Point(30,20), 40, 20, "QUIT")
    # Activate the button
    quitbutton.activate()

    # Create a roll button that randomizes the 5 dice values from Button class
    rollbutton = Button(win, Point(350,720), 70, 40, "ROLL")
    # Activate the button
    rollbutton.activate()
    # Keep track of how many times the roll button is clicked with
        # variable 'rollcount'
    rollcount = 0

    # Create 5 buttons for each die from Button class
    die1button = Button(win, Point(80,120), 70, 70, "")
    die2button = Button(win, Point(215,120), 70, 70, "")
    die3button = Button(win, Point(350,120), 70, 70, "")
    die4button = Button(win, Point(485,120), 70, 70, "")
    die5button = Button(win, Point(620,120), 70, 70, "")

    # Create 5 dice from Die class 
    die1 = Die(win, Point(80,120), 70, 70, 6, 1)
    die2 = Die(win, Point(215,120), 70, 70, 6, 2)
    die3 = Die(win, Point(350,120), 70, 70, 6, 3)
    die4 = Die(win, Point(485,120), 70, 70, 6, 4)
    die5 = Die(win, Point(620,120), 70, 70, 6, 5)

    # Create 13 buttons for each category from Button class
    oneshand = Button(win, Point(270,325), 80, 30, "")
    twoshand = Button(win, Point(270,370), 80, 30, "")
    threeshand = Button(win, Point(270,415), 80, 30, "")
    fourshand = Button(win, Point(270,460), 80, 30, "")
    fiveshand = Button(win, Point(270,505), 80, 30, "")
    sixeshand = Button(win, Point(270,550), 80, 30, "")
    threeofakind = Button(win, Point(530,325), 80, 30, "")
    fourofakind = Button(win, Point(530,370), 80, 30, "")
    fullhouse = Button(win, Point(530,415), 80, 30, "")
    smallstraight = Button(win, Point(530,460), 80, 30, "")
    largestraight = Button(win, Point(530,505), 80, 30, "")
    chance = Button(win, Point(530,550), 80, 30, "")
    yahtzee = Button(win, Point(530,595), 80, 30, "")

    # Create a score cell for each category from ScoreCell class
        # Include, sum, bonus, and total - not buttons, but to
        # be evaluated at the end of the game
    onesscore = ScoreCell(win, Point(270,325), 80, 30, "")
    twosscore = ScoreCell(win, Point(270,370), 80, 30, "")
    threesscore = ScoreCell(win, Point(270,415), 80, 30, "")
    foursscore = ScoreCell(win, Point(270,460), 80, 30, "")
    fivesscore = ScoreCell(win, Point(270,505), 80, 30, "")
    sixesscore = ScoreCell(win, Point(270,550), 80, 30, "")
    sumscore = ScoreCell(win, Point(270, 595), 80, 30, "")
    bonusscore = ScoreCell(win, Point(270,640), 80, 30, "")
    threeofakindscore = ScoreCell(win, Point(530,325), 80, 30, "")
    fourofakindscore = ScoreCell(win, Point(530,370), 80, 30, "")
    fullhousescore = ScoreCell(win, Point(530,415), 80, 30, "")
    smallstraightscore = ScoreCell(win, Point(530,460), 80, 30, "")
    largestraightscore = ScoreCell(win, Point(530,505), 80, 30, "")
    chancescore = ScoreCell(win, Point(530,550), 80, 30, "")
    yahtzeescore = ScoreCell(win, Point(530,595), 80, 30, "")
    totalscore = ScoreCell(win, Point(530,640), 80, 30, "")


    # A round ends at 3 clicks on the roll button
    while rollcount <= 3:
        # Expect a user click and store in variable 'pt'
        pt = win.getMouse()
        # Detect if the roll button is clicked - it MUST be active
            # to continue
        if rollbutton.activeandclicked(pt):
            # Add 1 to the 'rollcount' variable to keep track of how many
            # times the roll button is clicked
            rollcount += 1
            # If the roll button is clicked once in the round:
                # Activate the roll button
                # Activate all of the dice
                # Roll all of the dice
            if rollcount == 1:
                rollbutton.activate()
                die1button.activate()
                die2button.activate()
                die3button.activate()
                die4button.activate()
                die5button.activate()
                die1.roll()
                die2.roll()
                die3.roll()
                die4.roll()
                die5.roll()
                # Check each scorecell category; if the string is empty,
                # activate it, but if the string isn't empty, deactivate it
                if onesscore.label.getText() == "":
                    oneshand.activate()
                elif onesscore.label.getText() != "":
                    oneshand.deactivate()
                if twosscore.label.getText() == "":
                    twoshand.activate()
                elif twosscore.label.getText() != "":
                    twoshand.deactivate()
                if threesscore.label.getText() == "":
                    threeshand.activate()
                elif threesscore.label.getText() != "":
                    threeshand.deactivate()
                if foursscore.label.getText() == "":
                    fourshand.activate()
                elif foursscore.label.getText() != "":
                    fourshand.deactivate()
                if fivesscore.label.getText() == "":
                    fiveshand.activate()
                elif fivesscore.label.getText() != "":
                    fiveshand.deactivate()
                if sixesscore.label.getText() == "":
                    sixeshand.activate()
                elif sixesscore.label.getText() != "":
                    sixeshand.deactivate()
                if threeofakindscore.label.getText() == "":
                    threeofakind.activate()
                elif threeofakindscore.label.getText() != "":
                    threeofakind.deactivate()
                if fourofakindscore.label.getText() == "":
                    fourofakind.activate()
                elif fourofakindscore.label.getText() != "":
                    fourofakind.deactivate()
                if fullhousescore.label.getText() == "":
                    fullhouse.activate()
                elif fullhousescore.label.getText() != "":
                    fullhouse.deactivate()
                if smallstraightscore.label.getText() == "":
                    smallstraight.activate()
                elif smallstraightscore.label.getText() != "":
                    smallstraight.deactivate()
                if largestraightscore.label.getText() == "":
                    largestraight.activate()
                elif largestraightscore.label.getText() != "":
                    largestraight.deactivate()
                if chancescore.label.getText() == "":
                    chance.activate()
                elif chancescore.label.getText() != "":
                    chance.deactivate()
                if (yahtzeescore.label.getText() == "" or
                    yahtzeescore.label.getText() != ""):
                    yahtzee.activate()

                # Set the message box to tell the user to roll the dice
                    # using the roll button
                # Also let the user know they can click on a dice now and it
                    # will NOT roll (hold)
                instructions.setText("2 more rolls left! Click on a die to hold it - the border for held die will disappear.")

            # If the roll button is clicked twice in the round:
                # Activate the roll button
                # Check each scorecell category; if the string is empty,
                # activate it, but if the string isn't empty, deactivate it
            elif rollcount == 2:
                rollbutton.activate()
                if onesscore.label.getText() == "":
                    oneshand.activate()
                elif onesscore.label.getText() != "":
                    oneshand.deactivate()
                if twosscore.label.getText() == "":
                    twoshand.activate()
                elif twosscore.label.getText() != "":
                    twoshand.deactivate()
                if threesscore.label.getText() == "":
                    threeshand.activate()
                elif threesscore.label.getText() != "":
                    threeshand.deactivate()
                if foursscore.label.getText() == "":
                    fourshand.activate()
                elif foursscore.label.getText() != "":
                    fourshand.deactivate()
                if fivesscore.label.getText() == "":
                    fiveshand.activate()
                elif fivesscore.label.getText() != "":
                    fiveshand.deactivate()
                if sixesscore.label.getText() == "":
                    sixeshand.activate()
                elif sixesscore.label.getText() != "":
                    sixeshand.deactivate()
                if threeofakindscore.label.getText() == "":
                    threeofakind.activate()
                elif threeofakindscore.label.getText() != "":
                    threeofakind.deactivate()
                if fourofakindscore.label.getText() == "":
                    fourofakind.activate()
                elif fourofakindscore.label.getText() != "":
                    fourofakind.deactivate()
                if fullhousescore.label.getText() == "":
                    fullhouse.activate()
                elif fullhousescore.label.getText() != "":
                    fullhouse.deactivate()
                if smallstraightscore.label.getText() == "":
                    smallstraight.activate()
                elif smallstraightscore.label.getText() != "":
                    smallstraight.deactivate()
                if largestraightscore.label.getText() == "":
                    largestraight.activate()
                elif largestraightscore.label.getText() != "":
                    largestraight.deactivate()
                if chancescore.label.getText() == "":
                    chance.activate()
                elif chancescore.label.getText() != "":
                    chance.deactivate()
                if (yahtzeescore.label.getText() == "" or
                    yahtzeescore.label.getText() != ""):
                    yahtzee.activate()

                # Set the message box to tell the user to roll the dice
                    # using the roll button
                # Also let the user know they can click on a dice now and it
                    # will NOT roll (hold)
                instructions.setText("1 more roll left! Click on a die to hold it - the border for held die will disappear.")
                
            # If the roll button is clicked twice in the round:
                # Deactivate the roll button
                # Check each scorecell category; if the string is empty,
                # activate it, but if the string isn't empty, deactivate it
            elif rollcount == 3:
                rollbutton.deactivate()
                if onesscore.label.getText() == "":
                    oneshand.activate()
                elif onesscore.label.getText() != "":
                    oneshand.deactivate()
                if twosscore.label.getText() == "":
                    twoshand.activate()
                elif twosscore.label.getText() != "":
                    twoshand.deactivate()
                if threesscore.label.getText() == "":
                    threeshand.activate()
                elif threesscore.label.getText() != "":
                    threeshand.deactivate()
                if foursscore.label.getText() == "":
                    fourshand.activate()
                elif foursscore.label.getText() != "":
                    fourshand.deactivate()
                if fivesscore.label.getText() == "":
                    fiveshand.activate()
                elif fivesscore.label.getText() != "":
                    fiveshand.deactivate()
                if sixesscore.label.getText() == "":
                    sixeshand.activate()
                elif sixesscore.label.getText() != "":
                    sixeshand.deactivate()
                if threeofakindscore.label.getText() == "":
                    threeofakind.activate()
                elif threeofakindscore.label.getText() != "":
                    threeofakind.deactivate()
                if fourofakindscore.label.getText() == "":
                    fourofakind.activate()
                elif fourofakindscore.label.getText() != "":
                    fourofakind.deactivate()
                if fullhousescore.label.getText() == "":
                    fullhouse.activate()
                elif fullhousescore.label.getText() != "":
                    fullhouse.deactivate()
                if smallstraightscore.label.getText() == "":
                    smallstraight.activate()
                elif smallstraightscore.label.getText() != "":
                    smallstraight.deactivate()
                if largestraightscore.label.getText() == "":
                    largestraight.activate()
                elif largestraightscore.label.getText() != "":
                    largestraight.deactivate()
                if chancescore.label.getText() == "":
                    chance.activate()
                elif chancescore.label.getText() != "":
                    chance.deactivate()
                if (yahtzeescore.label.getText() == "" or
                    yahtzeescore.label.getText() != ""):
                    yahtzee.activate()

                # Set the message box to tell the user to click on a
                    # scorecell category 
                instructions.setText("Click on a score category to score your hand.")

            # Check if each die button's label is active:
                # If so, roll the die
                # Assign the die's value to a variable
            if die1button.active == True:
                die1.roll()
                d1 = die1.getValue()
            if die2button.active == True:
                die2.roll()
                d2 = die2.getValue()
            if die3button.active == True:
                die3.roll()
                d3 = die3.getValue()
            if die4button.active == True:
                die4.roll()
                d4 = die4.getValue()
            if die5button.active == True:
                die5.roll()
                d5 = die5.getValue()

        # If a die is clicked, check whether it is active or not
            # If active, deactivate the die's button
            # If not active, activate the die's button
        for i in (die1button, die2button, die3button, die4button,
                  die5button):
            if (die1button.clicked(pt)):
                if die1button.active == True:
                    die1button.deactivate()
                elif die1button.active == False:
                    die1button.activate()
            elif (die2button.clicked(pt)):
                if die2button.active == True:
                    die2button.deactivate()
                elif die2button.active == False:
                    die2button.activate()
            elif (die3button.clicked(pt)):
                if die3button.active == True:
                    die3button.deactivate()
                elif die3button.active == False:
                    die3button.activate()
            elif (die4button.clicked(pt)):
                if die4button.active == True:
                    die4button.deactivate()
                elif die4button.active == False:
                    die4button.activate()
            elif (die5button.clicked(pt)):
                if die5button.active == True:
                    die5button.deactivate()
                elif die5button.active == False:
                    die5button.activate()
                    
        # Detect which category is clicked - it MUST be active - and
            # display calculated score
        # Once chosen, all other categories (self included) are deactivated
        # Use the appropriate method from the ScoreCell class
        # Reset the roll count to restart the conditional
        # Update instructions to direct user to the roll button for the
            # next round
        if oneshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            onesscore.onesValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif twoshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            twosscore.twosValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif threeshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            threesscore.threesValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif fourshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            foursscore.foursValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif fiveshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            fivesscore.fivesValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif sixeshand.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            sixesscore.sixesValues(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif threeofakind.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            threeofakindscore.threeOfAKind(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif fourofakind.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            fourofakindscore.fourOfAKind(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif fullhouse.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            fullhousescore.fullHouse(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif smallstraight.activeandclicked(pt):
            # Exception for joker rule - check if it qualifies as a joker
                # Yahtzee and already 0
            if (d1 == d2 == d3 == d4 == d5 and yahtzeescore.label.getText()
                == 0):
                # Set score label to be 30
                smallstraightscore.label.setText(30)
                # Deactive all lower values
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
            # Exception for joker rule - check if it qualifies as a joker
                # Yahtzee and already 50
            elif (d1 == d2 == d3 == d4 == d5 and yahtzeescore.label.getText()
                  == 50):
                # Set score label to be 30
                smallstraightscore.label.setText(30)
                # Deactive all lower values
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
            # Otherwise score small straight normally
            else:
                oneshand.deactivate()
                twoshand.deactivate()
                threeshand.deactivate()
                fourshand.deactivate()
                fiveshand.deactivate()
                sixeshand.deactivate()
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                yahtzee.deactivate()
                smallstraightscore.smallStraight(d1, d2, d3, d4, d5)
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
        elif largestraight.activeandclicked(pt):
            # Exception for joker rule - check if it qualifies as a joker
                # Yahtzee and already 0
            if (d1 == d2 == d3 == d4 == d5 and yahtzeescore.label.getText()
                == 0):
                # Set score label to be 40
                largestraightscore.label.setText(40)
                # Deactive all lower values
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
            # Exception for joker rule - check if it qualifies as a joker
                # Yahtzee and already 50
            elif (d1 == d2 == d3 == d4 == d5 and yahtzeescore.label.getText()
                  == 50):
                # Set score label to be 40
                largestraightscore.label.setText(40)
                # Deactive all lower values
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
            else:
                oneshand.deactivate()
                twoshand.deactivate()
                threeshand.deactivate()
                fourshand.deactivate()
                fiveshand.deactivate()
                sixeshand.deactivate()
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                yahtzee.deactivate()
                largestraightscore.largeStraight(d1, d2, d3, d4, d5)
                rollcount = 0
                instructions.setText("Scored! Click the roll button for the next round.")
                rollbutton.activate()
        elif chance.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            chancescore.chance(d1, d2, d3, d4, d5)
            rollcount = 0
            instructions.setText("Scored! Click the roll button for the next round.")
            rollbutton.activate()
        elif yahtzee.activeandclicked(pt):
            oneshand.deactivate()
            twoshand.deactivate()
            threeshand.deactivate()
            fourshand.deactivate()
            fiveshand.deactivate()
            sixeshand.deactivate()
            threeofakind.deactivate()
            fourofakind.deactivate()
            fullhouse.deactivate()
            smallstraight.deactivate()
            largestraight.deactivate()
            chance.deactivate()
            yahtzee.deactivate()
            # First check if the Yahtzee is true - five same dice values
            if d1 == d2 == d3 == d4 == d5:
                # Deactivate all score cell buttons
                oneshand.deactivate()
                twoshand.deactivate()
                threeshand.deactivate()
                fourshand.deactivate()
                fiveshand.deactivate()
                sixeshand.deactivate()
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                yahtzee.deactivate()
                # If so, check if the Yahtzee is ALREADY scored as 0
                if yahtzeescore.label.getText() == 0:
                    # Also deactive the roll button here
                    rollbutton.deactivate()
                    # If so, go through each possible die value 1-6:
                        # If its corresponding upper Value category is
                            # empty, only activate that category
                        # If its corresponding upper Value category is
                            # NOT empty, continue to joker scenario
                    if d1 == 1:
                        if onesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the ones category!")
                            oneshand.activate()
                        elif onesscore.label.getText() != "":
                            # Let the user know that they can user a joker 
                                # by updating the message box
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            # If the lower value categories are available,
                                # activate them
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 2:
                        if twosscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the twos category!")
                            twoshand.activate()
                        elif twosscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 3:
                        if threesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the threes category!")
                            threeshand.activate()
                        elif threesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 4:
                        if foursscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the fours category!")
                            fourshand.activate()
                        elif foursscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 5:
                        if fivesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the fives category!")
                            fiveshand.activate()
                        elif fivesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 6:
                        if sixesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the sixes category!")
                            sixeshand.activate()
                        elif sixesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                # If so, check if the Yahtzee is ALREADY scored as 50
                elif yahtzeescore.label.getText() == 50:
                    # Also deactive the roll button here
                    rollbutton.deactivate()
                    # If so, go through each possible die value 1-6:
                        # If its corresponding upper Value category is
                            # empty, only activate that category
                        # If its corresponding upper Value category is
                            # NOT empty, continue to joker scenario
                    if d1 == 1:
                        if onesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the ones category!")
                            oneshand.activate()
                        elif onesscore.label.getText() != "":
                            # Let the user know that they can user a joker 
                                # by updating the message box
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            # If the lower value categories are available,
                                # activate them
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 2:
                        if twosscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the twos category!")
                            twoshand.activate()
                        elif twosscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 3:
                        if threesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the threes category!")
                            threeshand.activate()
                        elif threesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 4:
                        if foursscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the fours category!")
                            fourshand.activate()
                        elif foursscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 5:
                        if fivesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the fives category!")
                            fiveshand.activate()
                        elif fivesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    elif d1 == 6:
                        if sixesscore.label.getText() == "":
                            instructions.setText("No joker - you must score in the sixes category!")
                            sixeshand.activate()
                        elif sixesscore.label.getText() != "":
                            instructions.setText("Joker! Click on one of the available categories to score your hand.")
                            if threeofakindscore.label.getText() == "":
                                threeofakind.activate()
                            if fourofakindscore.label.getText() == "":
                                fourofakind.activate()
                            if fullhousescore.label.getText() == "":
                                fullhouse.activate()
                            if smallstraightscore.label.getText() == "":
                                smallstraight.activate()
                            if largestraightscore.label.getText() == "":
                                largestraight.activate()
                            if chancescore.label.getText() == "":
                                chance.activate()
                            # If the lower value categories aren't available,
                                # Activate the roll button to start the next
                                    # round
                                # Update instructions to start next round
                            if (threeofakindscore.label.getText() != "" and
                                fourofakindscore.label.getText() != "" and
                                fullhousescore.label.getText() != "" and
                                smallstraightscore.label.getText() != "" and
                                largestraightscore.label.getText() != "" and
                                chancescore.label.getText() != ""):
                                instructions.setText("Oops! No joker available. Click the roll button to continue to the next round.")
                                # Update the instructions so the user clicks the roll button
                                rollcount = 0
                                # Activate the roll button
                                rollbutton.activate()
                    # Convert the current Yahtzee scorecell's label
                        # to an integer
                    yahtzeeint = int(yahtzeescore.label.getText())
                    # Add a 100 point bonus
                    yahtzeeint += 100
                    # Update the Yahtzee scorecell's label with the new
                        # value
                    yahtzeescore.label.setText(yahtzeeint)
                # If so, check if the value is ALREADY over 50
                    # Not 0, not 50, and not empty
                elif yahtzeescore.label.getText() != "":
                    # Also deactive the roll button here
                    rollbutton.deactivate()
                    # Compare the current yahtzee score by saving the label 
                        # to a variable and setting it to an integer
                    yahtzeeint = int(yahtzeescore.label.getText())
                    yahtzeeint += 100
                    yahtzeescore.label.setText(yahtzeeint)
                    # Reset the round by setting the roll button clicks to 0
                    rollcount = 0
                    # Update the instructions so the user clicks the roll button
                    instructions.setText("Scored! Click the roll button for the next round.")
                    # Activate the roll button
                    rollbutton.activate()
                # If so, check if the Yahtzee is ALREADY empty
                elif yahtzeescore.label.getText() == "":
                    # Also deactive the roll button here
                    rollbutton.deactivate()
                    yahtzeescore.yahtzeeFiveOfAKind(d1, d2, d3, d4, d5)
                    # Reset the round by setting the roll button clicks to 0
                    rollcount = 0
                    # Update the instructions so the user clicks the roll button
                    instructions.setText("Scored! Click the roll button for the next round.")
                    # Activate the roll button
                    rollbutton.activate()
            # If it is not a Yahtzee and the Yahtzee category is not empty
            elif (not d1 == d2 == d3 == d4 == d5 and
                  yahtzeescore.label.getText() != ""):
                # Deactivate the Yahtzee button
                yahtzee.deactivate()
                # Deactiveate the roll button
                rollbutton.deactivate()
                # Give the user an error message and allow them to select
                  # another category if it is available
                # Activate the ones with an empty label string
                instructions.setText("Not a yahtzee! You already scored here, choose another category.")
                if onesscore.label.getText() == "":
                    oneshand.activate()
                if twosscore.label.getText() == "": 
                    twoshand.activate()
                if threesscore.label.getText() == "":
                    threeshand.activate()
                if foursscore.label.getText() == "":
                    fourshand.activate()
                if fivesscore.label.getText() == "":
                    fiveshand.activate()
                if sixesscore.label.getText() == "":
                    sixeshand.activate()
                if threeofakindscore.label.getText() == "":
                    threeofakind.activate()
                if fourofakindscore.label.getText() == "":
                    fourofakind.activate()
                if fullhousescore.label.getText() == "":
                    fullhouse.activate()
                if smallstraightscore.label.getText() == "":
                    smallstraight.activate()
                if largestraightscore.label.getText() == "":
                    largestraight.activate()
                if chancescore.label.getText() == "":
                    chance.activate()
            # If it is not a Yahtzee and the Yahtzee category is empty
            elif (not d1 == d2 == d3 == d4 == d5 and
                  yahtzeescore.label.getText() == ""):
                # Deactivate all score cells
                oneshand.deactivate()
                twoshand.deactivate()
                threeshand.deactivate()
                fourshand.deactivate()
                fiveshand.deactivate()
                sixeshand.deactivate()
                threeofakind.deactivate()
                fourofakind.deactivate()
                fullhouse.deactivate()
                smallstraight.deactivate()
                largestraight.deactivate()
                chance.deactivate()
                yahtzee.deactivate()
                # Set the Yahtzee scorecell score as 0
                yahtzeescore.label.setText(0)
                # Reset the round by setting the roll button clicks to 0
                rollcount = 0
                # Update the instructions so the user clicks the roll button
                instructions.setText("Scored! Click the roll button for the next round.")
                # Activate the roll button
                rollbutton.activate()

        # Check labels to see if all category scorecells have values 
        if (onesscore.label.getText() != "" and twosscore.label.getText() !=
            "" and threesscore.label.getText() != "" and
            foursscore.label.getText() != "" and fivesscore.label.getText()
            != "" and sixesscore.label.getText() != "" and
            threeofakindscore.label.getText() != "" and
            fourofakindscore.label.getText() != "" and
            fullhousescore.label.getText() != "" and
            smallstraightscore.label.getText() != "" and
            largestraightscore.label.getText() != "" and
            chancescore.label.getText() != "" and
            yahtzeescore.label.getText() != ""):
            # Deactivate the roll button
            rollbutton.deactivate()
            # Sum the upper values - get through label - and put into 
            # variable 'valsum', then into the sum scorecell
            valsum = (int(onesscore.label.getText()) +
                      int(twosscore.label.getText()) +
                      int(threesscore.label.getText()) +
                      int(foursscore.label.getText()) +
                      int(fivesscore.label.getText()) +
                      int(sixesscore.label.getText()))
            # Update the sum scorecell's label with 'valsum' value
            sumscore.label.setText(valsum)
            # Create a new variable for the total sum 'totalsum'
            totalsum = valsum
            # Check if the sum of the upper values is >= 63; if so:
                # Add a bonus of 35 points to the total sum
                # Otherwise, no bonus
            if valsum >= 63:
                bonusscore.label.setText(35)
                totalsum += 35
            else:
                bonusscore.label.setText(0)
            # Add the rest of the category scorecell values to 'totalsum'
            totalsum = (totalsum + int(threeofakindscore.label.getText()) +
                          int(fourofakindscore.label.getText()) +
                          int(fullhousescore.label.getText()) +
                          int(smallstraightscore.label.getText()) +
                          int(largestraightscore.label.getText()) +
                          int(chancescore.label.getText()) +
                          int(yahtzeescore.label.getText()))
            # Update the totalscore scorecell's label with 'totalsum' value
            totalscore.label.setText(totalsum)
            # Update the instructions for the user to play again or quit
            instructions.setText("Good game! Click the 'Play Again' button to play again. Click the 'Quit' button to quit.")
            # Create a new button 'playagain' and activate it
            playagain = Button(win, Point(350, 770), 80, 40, "Play Again")
            playagain.activate()
            # If the 'playagain' button is both active and clicked
            if playagain.activeandclicked(pt):
                # Deactivate the 'playagain' button
                playagain.deactivate()
                # Add 1 to the number of games counter
                games = games + 1
                # Update the number of games counter text
                numgames.setText("Number of Games Played: " + str(games))
                # Check if the new score 'totalsum' is greater than the
                    # existing score 'newhighscore'
                if totalsum > newhighscore:
                    # If so, set 'newhighscore' to the new value of
                        # 'totalsum'
                    newhighscore = totalsum
                    # Update the high score tracker text
                    highscore.setText("High Score: " + str(newhighscore))
                elif totalsum < newhighscore:
                    # If not, keep the original score 'newhighscore'
                    newhighscore = newhighscore
                # Update the instructions for the user to click the roll button
                instructions.setText("Click the Roll button to begin")
                # Reset all scorecells to an empty string
                onesscore.label.setText("")
                twosscore.label.setText("")
                threesscore.label.setText("")
                foursscore.label.setText("")
                fivesscore.label.setText("")
                sixesscore.label.setText("")
                sumscore.label.setText("")
                bonusscore.label.setText("")
                threeofakindscore.label.setText("")
                fourofakindscore.label.setText("")
                fullhousescore.label.setText("")
                smallstraightscore.label.setText("")
                largestraightscore.label.setText("")
                chancescore.label.setText("")
                yahtzeescore.label.setText("")
                totalscore.label.setText("")
                # Activate the roll button
                rollbutton.activate()
                
        # At any time if the user clicks the quit button, close the window
        if quitbutton.clicked(pt):
            win.close()

 
# Call the function
main()



    
    
    
