from sense_hat import SenseHat
import time
import random
import threading

sense = SenseHat()

sense.clear()

#Defining colors for player 1 and player 2
b = [0, 0, 0]
g = [0, 255, 0]
r = [255, 0, 0]

oneP1 = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

twoP1 = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,g,g,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,g,g,b,b,
b,b,b,b,g,g,b,b,
b,b,b,b,b,b,b,b,
]

threeP1 = [
g,g,b,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,g,g,
b,b,b,b,b,b,g,g,
]

fourP1 = [
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,g,g,b,b,g,g,b,
b,g,g,b,b,g,g,b,
b,b,b,b,b,b,b,b,
]

fiveP1 = [
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
]

sixP1 = [
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
b,b,b,b,b,b,b,b,
g,g,b,b,b,b,g,g,
g,g,b,b,b,b,g,g,
]

oneP2 = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

twoP2 = [
b,b,b,b,b,b,b,b,
b,r,r,b,b,b,b,b,
b,r,r,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,r,r,b,b,
b,b,b,b,r,r,b,b,
b,b,b,b,b,b,b,b,
]

threeP2 = [
r,r,b,b,b,b,b,b,
r,r,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,r,r,
b,b,b,b,b,b,r,r,
]

fourP2 = [
b,b,b,b,b,b,b,b,
b,r,r,b,b,r,r,b,
b,r,r,b,b,r,r,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,r,r,b,b,r,r,b,
b,r,r,b,b,r,r,b,
b,b,b,b,b,b,b,b,
]

fiveP2 = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

sixP2 = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]


point = None

def roll_dice(color):
    """
    Roll dice function that will return rolled dice result with coordinated color
    """
    if color == "green":

        r = random.randint(1,6)
        if r == 1:
            sense.set_pixels(oneP1)
        elif r == 2:
            sense.set_pixels(twoP1)
        elif r == 3:
            sense.set_pixels(threeP1)
        elif r == 4:
            sense.set_pixels(fourP1)
        elif r == 5:
            sense.set_pixels(fiveP1)
        elif r == 6:
            sense.set_pixels(sixP1)
        
    elif color == "red":

        r = random.randint(1,6)
        if r == 1:
            sense.set_pixels(oneP2)
        elif r == 2:
            sense.set_pixels(twoP2)
        elif r == 3:
            sense.set_pixels(threeP2)
        elif r == 4:
            sense.set_pixels(fourP2)
        elif r == 5:
            sense.set_pixels(fiveP2)
        elif r == 6:
            sense.set_pixels(sixP2)
    
    return r

def die_engine(color):
    """
    Dice game engine to determine the roll of the dice with sensehat accelerometer and return dice result value
    """
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)
    point = 0

   
    if x > 1.4 or y > 1.4 or z > 1.4:
        point = roll_dice(color)
        print("Number rendered:" + str(point))
        time.sleep(1)        

     
    return point
      
           
      

       
def get_random_num(color):
    """
    Main program interface
    """
    score = 0
    while True:
        score = die_engine(color) + score
        if score > 0:
            break
    return score