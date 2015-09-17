from random import randint

# Class for rolling dice, returns as either a single sum of dice rolls or list of dice rolls

class dice_roll(object):
    def __init__(self):
        self.output = 0
        self.output_list = []

# Function for rolling attributes will roll 4 d6s and drop lowest
    def stat_roll(self):
        rolls = []
        return_roll = 0
        
        for i in range(0, 4):
            rolls.append(randint(1,6))
        rolls = sorted(rolls)
        
        for i in range(1, 4):
            return_roll += rolls[i]
        
        return return_roll
        

# Rolls a certain dice a certain number of times and returns the sum before clearing self.output    
    def roll(self, roll, times = 1):
        for i in list(range(0,times)):
            if roll == 4:
                self.output += (randint(1,4))
            elif roll == 6:
                self.output += (randint(1,6))
            elif roll == 8:
                self.output += (randint(1,8))
            elif roll == 10:
                self.output += (randint(1,10))
            elif roll == 12:
                self.output += (randint(1,12))
            elif roll == 20:
                self.output += (randint(1,20))
            elif roll == 100:
                self.output += (randint(1,100))
            else:
                return 0
        returned = self.output
        self.clean_roll()
        return returned     

# Rolls a dice a certain number of times and returns a list of rolls before clearing self.output_list        
    def roll_list(self, roll, times = 1):
        for i in list(range(0,times)):
            if roll == 4:
                self.output_list.append(randint(1,4))
            elif roll == 6:
                self.output_list.append(randint(1,6))
            elif roll == 8:
                self.output_list.append(randint(1,8))
            elif roll == 10:
                self.output_list.append(randint(1,10))
            elif roll == 12:
                self.output_list.append(randint(1,12))
            elif roll == 20:
                self.output_list.append(randint(1,20))
            elif roll == 100:
                self.output_list.append(randint(1,100))
            else:
                return 0
        returned = self.output_list
        self.clean_roll()
        return returned
    
    def clean_roll(self):
        self.output_list = []
        self.output = 0