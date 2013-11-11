#. "Guess the number" mini-project
#. Author: @dspk

#. Download and install SimpleGUICS2Pygame before import below
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

#. Initialize global variables 
num_range = 100 
max_guess = 7
count = 0

#. Define event handlers for control panel
def init():
    global count
    """print initial content"""
    print "New game."
    count = 0
    
def range100():
    # button that changes range to range [0,100) and restarts
    """generate random secret number between 0 to 100"""
    global num_range, max_guess
    num_range = random.randrange(0, 100)
    max_guess = 7
    init() 
        
def range1000():
    # button that changes range to range [0,1000) and restarts
    """generate random secret number between 0 to 100"""
    global num_range, max_guess
    num_range = random.randrange(0, 1000)
    max_guess = 10
    init()
    
def get_input(guess):
    global num_range, max_guess, count
    # main game logic goes here	
    num_guess = float(guess)
    count += 1
    if max_guess - count < 0:
        print "You have exceeded your chances."
    elif num_guess > num_range:
        print "Guess was", num_guess
        print "Number of remaining guesses is", max_guess - count
        print "Lower!"
    elif num_guess  < num_range:
        print "Guess was", num_guess
        print "Number of remaining guesses is", max_guess - count
        print "Higher!"
    else:
        print "Guess was", num_guess
        print "Number of remaining guesses is", max_guess - count
        print "Correct!"
        
         
#. Create frame
frame = simplegui.create_frame("Guess the number", 300, 300)


#. Register event handlers for control elements
button1 = frame.add_button("Range is [0, 100)", range100, 200)
button1 = frame.add_button("Range is [0, 1000)", range1000, 200)
inp = frame.add_input("Enter a guess", get_input, 200)

#. Start frame
frame.start()












