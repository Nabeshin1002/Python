from Dice_Roll import dice_roll
import configparser

# Contains functions for creating and storing character values        
class stats(object):
    def __init__(self):   
        self.dice = dice_roll()
        self.character = {'name': "",'level': 1, 'race': "", 'hp': 0, "Armor": 10, 'str': 0, 'str_base' : 0, 'dex': 0, 'dex_base' : 0, 'con': 0, 'con_base' : 0, 'int': 0, 'int_base' : 0,  'wis' : 0, 'wis_base' : 0, 'cha' : 0, 'cha_base' : 0}
        self.score_mods = configparser.ConfigParser()
        self.score_mod.sections()
        self.score_mod.read('score_mod.ini')
        self.race_mod = configparser.ConfigParser()
        self.race_mod.sections()
        self.race_mod.read('Racial_Modifiers.ini')

    def start(self):
        print("Welcome to Super Character Maker 9001!")
        print("Lets make your character!")
        print("How do you want to choose attributes?\n")
        print("1. Random Rolls (3 to 18)")
        print("2. Point Buy (8 to 15)")
        
        choice = 0
        while choice != 1 and choice != 2:
            try:
                choice =  int(input("Pick a system: "))
            except:
                print("That's not a valid choice, try again.\n")
        
        if choice == 1:
            self.create_char()
        if choice == 2:
            self.create_char_pb()
        
        print("Here is your final character: \n")
        self.print_char()
        

# Character creation function using dice rolls
    def create_char(self):
        attribute = ['Strength', 'Dexterity', 'Consitution', 'Intelligence', 'Wisdom', 'Charisma']
        att_base = ['str_base', 'dex_base', 'con_base', 'int_base', 'wis_base', 'cha_base']
        rolls = []          
        count = 0
        
        self.character['name'] = input("What is your name: ")
        print(" ")
        
        while count < 6:
            rolls.append(self.dice.stat_roll())
            count += 1
            
        rolls = sorted(rolls)
        
        print("Here are your rolls:")
        print(rolls)
        print(" ")
        
        print("We are now going to assign rolls to attributes.\n")
        count = 0
        while count < 6:
            print("Roll Selection: ")
            for i in range(0, len(rolls)):
                print("{}. {}".format(i + 1, rolls[i]))
            
            roll_input = input("Select a roll: ")
            
            print(" ")
            print("Attribute Selection: ")
            for i in range(0, len(attribute)):
                print("{}. {}".format(i + 1, attribute[i]))
            att_input = input("Select an attribute: ")
            
            print(" ")
            self.character[att_base[int(att_input) - 1]] = int(rolls[int(roll_input) - 1])
            
            att_base.remove(att_base[int(att_input) - 1])
            attribute.remove(attribute[int(att_input) - 1])
            rolls.remove(rolls[int(roll_input) -1])
            
            count += 1
                 
        self.base_stat()
        
        print("Here are your current attributes:")
        self.print_char()
        
        stat_ask = 'y'
        while stat_ask[0].lower() == 'y':
            stat_ask = input("Do you want to switch the values of two stats Y/N: ")
            print(" ")
            if stat_ask[0].lower() == 'n':
                break
            done = 0
            while done == 0:
                switch1 = input("Enter the abbreviation of the first stat please (ex. str): ")
                switch2 = input("Okay now the second: ")
                if self.stat_switch(switch1, switch2):
                    done = 1
                    self.print_char()
                    print(" ")
                else:
                    print("That didn't seem to work, try again! Remember to use the abbreviations!") 
        
        self.racial_modifier()
        self.base_stat()
        print(" ")

# Character creation using point buy
    def create_char_pb(self):
        pb = 27
        pb_cost = {8 : 0, 9 : 1, 10 : 2, 11 : 3, 12 : 4, 13 : 5, 14 : 7, 15 : 9}
        attribute = ['Strength', 'Dexterity', 'Consitution', 'Intelligence', 'Wisdom', 'Charisma']
        att_base = ['str_base', 'dex_base', 'con_base', 'int_base', 'wis_base', 'cha_base']
        
        self.character['name'] = input("What is your name: ")
        print(" ")        
        
        print("Welcome to Point Buy.")
        print("You have 27 points to put into attributes.")
        print("Here are the values for each attribute score:")
        for i in range(8, 16):
            print ("Attribute: {} -- Value: {}".format(i, pb_cost[i]))
        
        count = 0
        value = 0
        
        while count < 6:
            print("You have {} points left".format(pb))
            try:
                value = int(input("What do you want your {} to be: ".format(attribute[count])))
                if value >= 8 and value <= 15 and pb_cost[value] <= pb:
                    attribute[count] = value
                    pb -= pb_cost[value]
                    count += 1
                else:
                    print("Insufficient points\n")
            except:
                print("That is not a valid input please try again\n")
        
        for i in range(0,len(attribute)):
            self.character[att_base[i]] = attribute[i]
            
        print("Here are your current attributes: ")
        print_char()
        
        stat_ask = 'y'
        while stat_ask[0].lower() == 'y':
            stat_ask = input("Do you want to switch the values of two stats Y/N: ")
            print(" ")
            if stat_ask[0].lower() == 'n':
                break
            done = 0
            while done == 0:
                switch1 = input("Enter the abbreviation of the first stat please (ex. str): ")
                switch2 = input("Okay now the second: ")
                if self.stat_switch(switch1, switch2):
                    done = 1
                    self.print_char()
                    print(" ")
                else:
                    print("That didn't seem to work, try again! Remember to use the abbreviations!")        
        
        self.racial_modifier()    
        self.base_stat()

# Function for returning the number of an attribute, takes name of attribute, returns a value as an integer  
    def call_stat(self, stat):
        if self.test_input(stat):
            return int(self.character[stat])
        return

# Function for making sure race entered is valid, may not be being used anymore    
    def check_race(self):
        race_check = self.character['race']
        race_check = race_check.capitalize()
        self.character['race'] = race_check
        try:
            race_check = self.race_mod[self.character['race']]
        except:
            return False
        return True

# Function for assigning base attribute values to current attibute values    
    def base_stat(self):
        self.character['str'] = self.character['str_base']
        self.character['dex'] = self.character['dex_base']
        self.character['con'] = self.character['con_base']
        self.character['int'] = self.character['int_base']
        self.character['wis'] = self.character['wis_base']
        self.character['cha'] = self.character['cha_base']        

# Function for printing all character stats        
    def print_char(self):
        print("{} the level {} {}'s Stats:".format(self.character['name'],self.character['level'], self.character['race']))
        print("Strength: {}".format(self.character['str']))
        print("Dexterity: {}".format(self.character['dex']))
        print("Constitution: {}".format(self.character['con']))
        print("Intelligence: {}".format(self.character['int']))
        print("Wisdom: {}".format(self.character['wis']))
        print("Charisma: {}".format(self.character['cha']))
        print(" ")

# Function for switching two attributes, takes two attributes, returns T/F based on if inputs are valid        
    def stat_switch(self, stat1, stat2):
        if not self.test_input_stat(stat1):
            return False
        if not self.test_input_stat(stat2):
            return False
        
        switch_att1 = 0
        switch_att2 = 0
        att1 = stat1 
        att2 = stat2 
        
        att1 = att1[0:3].lower() + "_base"
        att2 = att2[0:3].lower() + "_base"
        
        switch_att1 = self.character[att1]
        switch_att2 = self.character[att2]
        
        self.character[att1] = switch_att2
        self.character[att2] = switch_att1 
        
        self.base_stat()
        
        return True

# Function for testing to make sure an attribute input is good, returns T/F    
    def test_input_stat(self, stat):
        stat = stat.lower()
        if stat == 'str' or stat == 'dex' or stat == 'con' or stat == 'int' or stat == 'wis' or stat == 'cha':
            return True
        elif stat == 'str_base' or stat == 'dex_base' or stat == 'con_base' or stat == 'int_base' or stat == 'wis_base' or stat == 'cha_base':
            return True
        return False

# Function for altering a single attribute takes the attribute and number to alter it by    
    def stat_alter(self, stat, num):
        if self.test_input_stat(stat):
            self.character[stat] += num

# Function for choosing a race and adding the racial modifiers, runs during character creation    
    def racial_modifier(self):
        races = self.race_mod['Base_Races']['race']
        races = races.split(",")
        print("Please choose a number for a race from the selection: ")        
        for i in range(0, len(races)):
            print("{}: {}".format(i+1, races[i]))
        
        race = 0
        race_test = False
        while not race_test:
            try:
                race = int(input("Enter number: "))
                if race > 0 and race <= len(races):
                    race_test = True
                else:
                    print("That is not a valid entry, please try again")
                    print(" ")                    
            except:
                print("That is not a valid entry, please try again")
                print(" ")
        
        try:
            sub_race = self.race_mod[races[int(race) - 1]]['subrace']
            sub_race = sub_race.split(",")
            print("Please choose a subrace: ")
            for i in range(0, len(sub_race)):
                print("{}: {}".format(i + 1, sub_race[i]))
                
            num = input("Enter number: ")
            sub_race = sub_race[int(num) - 1]
        
        except:
            sub_race = races[int(race) -1]            
        
        for key in self.race_mod[sub_race]:
            alter = self.race_mod[sub_race][key]
            self.character[key] += int(alter)
        
        self.character['race'] = sub_race.replace("_", " ")
        
class char_class(object):
    def __init__(self):
        self.dice = dice_roll()
        self.c_class = {class_1 : " ", class_2 : "", level_1 : 1, level_2: 0}
        self.race_mod = configparser.ConfigParser()
        self.race_mod.sections()
        self.race_mod.read('Classes.ini')
