from Dice_Roll import dice_roll
import configparser

class char_create(object):
    def __init__(self):
        self.stat = stats()
        self.counter = counters()
    
    def char(self):
        self.stat.create_char()
        
        self.stat.print_char()
        self.counter.print_counters()
        
class char_run(object):
    def __init__(self):
        self.stat = stats()
        self.counter = counters()
        self.status = 'alive'
        
    def start(self):
        print("Welcome to Super Character Maker 9001!")
        print("Lets make your character!")
        self.char()
        print(" ")
        stat_ask = input("Do you want to switch the values of two stats (Only one time!) Y/N: ")
        if stat_ask[0].lower() == 'y':
            print("Okay, you have one chance to switch two stats, which do you want to switch")
            done = 0
            while done == 0:
                switch1 = input("Enter the abbreviation of the first stat please (ex. str): ")
                switch2 = input("Okay now the second: ")
                if self.stat.stat_switch(switch1, switch2):
                    done = 1
                else:
                    print("That didn't seem to work, try again! Remember to use the abbreviations!")
        print(" ")
        print("Okay here are you new stats!")
        self.stat.print_char()
    
    def char(self):
        self.stat.create_char()
        
        self.stat.print_char()
        self.counter.print_counters()
        
    def status_check(self):
        if self.counter.return_counter('hp') <= 0:
            self.status = 'dead'
        elif self.counter.return_counter('hp') == self.counter.return_counter('hp_max'):
            self.status = 'healthy'
        elif self.counter.return_counter('hp') < self.counter.return_counter('hp_max'):
            self.status = 'wounded'
    
    def print_char(self):
        self.stat.print_char()
        print(" ")
        self.counter.print_counters()
        
    def counter_change(self, counter, value):
        if self.counter(counter, value):
            return True
        else:
            return False
      
class counters(object):
    
    def __init__(self):
        self.counters = {'hp' : 100, 'hp_max': 100,'mp' : 100, 'mp_max' : 100, 'sp' : 100, 'sp_max' : 100}
        
    def counters_max(self):
        self.counters['hp'] = self.counters['hp_max']
        self.counters['mp'] = self.counters['mp_max']
        self.counters['sp'] = self.counters['sp_max']
    
    def print_counters(self):
        print("Hit Points: {}".format(self.counters['hp']))
        print("Mana Points: {}".format(self.counters['mp']))
        print("Spirit Points: {}".format(self.counters['sp']))
        
    def return_counter(self, counter):
        if self.check_input(counter):
            return self.counters[counter]
    
    def check_input(self, counter):
        if counter.lower() == 'hp' or 'mp' or 'sp' or 'hp_max' or 'mp_max' or 'sp_max':
            return True
        else:
            return False
        
    def check_max(self, counter):
        check = counter
        check = str(check) + '_max'
        if self.counters[counter] <= self.counters[check]:
            return True
        else:
            return False
    
    def alter_counter(self, counter, value):
        if self.check_input(counter):
            if value.isdigit():
                if self.check_max(counter):
                    self.counters[counter] += value
                    return True
        return False
    
    def set_counter(self, counter, value):
        if self.check_input(counter):
            if value.isdigit():
                self.counters[counter] = value
        return
    
    def get_value(self, counter):
        if self.check_input(counter):
            return counters[counter]
        return
    
class stats(object):
    def __init__(self):   
        self.dice = dice_roll()
        self.character = {'name': "",'level' : 1, 'race': "", 'str': 0, "Armor" : 10, 'str_base' : 0, 'dex': 0, 'dex_base' : 0, 'con': 0, 'con_base' : 0, 'int': 0, 'int_base' : 0,  'wis' : 0, 'wis_base' : 0, 'cha' : 0, 'cha_base' : 0}
        self.race_mod = configparser.ConfigParser()
        self.race_mod.sections()
        self.race_mod.read('Racial_Modifiers.ini')

    def create_char(self):
        self.character['name'] = input("What is your name: ")
        

            
            
        self.character['str_base'] = self.dice.roll(6,3)
        self.character['str'] = self.character['str_base']
        self.character['dex_base'] = self.dice.roll(6,3)
        self.character['dex'] = self.character['dex_base']
        self.character['con_base'] = self.dice.roll(6,3)
        self.character['con'] = self.character['con_base']
        self.character['int_base'] = self.dice.roll(6,3)
        self.character['int'] = self.character['int_base']
        self.character['wis_base'] = self.dice.roll(6,3)
        self.character['wis'] = self.character['wis_base']
        self.character['cha_base'] = self.dice.roll(6,3)
        self.character['cha'] = self.character['cha_base']
        
        race = False
        while race != True:
            self.character['race'] = input("What is your race: ")        
            if self.check_race():
                race = True
            else:
                print("That is not a valid race, please input a valid race")
                print(" ")
        self.racial_modifier()
        self.base_stat()
    
    def call_stat(self, stat):
        if self.test_input(stat):
            return self.character[stat]
        return
    
    def check_race(self):
        race_check = self.character['race']
        race_check = race_check.capitalize()
        self.character['race'] = race_check
        try:
            race_check = self.race_mod[self.character['race']]
        except:
            return False
        return True
    
    def base_stat(self):
        self.character['str'] = self.character['str_base']
        self.character['dex'] = self.character['dex_base']
        self.character['con'] = self.character['con_base']
        self.character['int'] = self.character['int_base']
        self.character['wis'] = self.character['wis_base']
        self.character['cha'] = self.character['cha_base']        
        
    def print_char(self):
        print("{} the level {} {}'s Stats:".format(self.character['name'],self.character['level'], self.character['race']))
        print("Strength: {}".format(self.character['str']))
        print("Dexterity: {}".format(self.character['dex']))
        print("Constitution: {}".format(self.character['con']))
        print("Intelligence: {}".format(self.character['int']))
        print("Wisdom: {}".format(self.character['wis']))
        print("Charisma: {}".format(self.character['cha']))
        
    def stat_switch(self, stat1, stat2):
        if not self.test_input_stat(stat1):
            return False
        if not self.test_input_stat(stat2):
            return False
        
        switch_att1 = 0
        switch_att2 = 0
        att1 = stat1
        att2 = stat2
        
        att1 = att1[0:3].lower()
        att2 = att2[0:3].lower()
        
        switch_att1 = self.character[att1]
        switch_att2 = self.character[att2]
        
        self.character[att1] = switch_att2
        self.character[att2] = switch_att1 
        return True
    
    def test_input_stat(self, stat):
        stat = stat.lower()
        if stat == 'str' or stat == 'dex' or stat == 'con' or stat == 'int' or stat == 'wis' or stat == 'cha':
            return True
        elif stat == 'str_base' or stat == 'dex_base' or stat == 'con_base' or stat == 'int_base' or stat == 'wis_base' or stat == 'cha_base':
            return True
        return False
    
    def stat_alter(self, stat, num):
        if self.test_input_stat(stat):
            self.character[stat] += num
    
    def racial_modifier(self):
        for key in self.race_mod[self.character['race']]:
            alter = self.race_mod[self.character['race']][key]
            self.character[key] += int(alter)