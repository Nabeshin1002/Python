from random import randint
import sys
sys.setrecursionlimit(5000)

class Map(object):
    def __init__(self):
        self.Map = []

    def Map_Input(self):
        input_rows = ""
        input_columns = ""
        input_start = ""
        input_end = ""
        
# Main function that runs all other functions, returns nothing    
        print("We're going to make a map!")
        input_rows = input("How many rows do you want: ")
        input_columns =  input("How many columns do you want: ")
        if self.Check_Input(input_rows, input_columns):
            custom_start = input("Do you want a custom start / end? Y/N: ")
            if custom_start[0].lower() == 'y':    
                input_start = input("Where would you like to start, please put two numbers seperated by a comma within your range ex. 1,1: ")
                input_end = input("Where would you like to end: ")
                if self.Check_Start_End(input_start, input_end, input_rows, input_columns):
                    print ("Here we go!")
                    self.Build_Map(int(input_rows), int(input_columns), input_start, input_end)
                else:
                    print("That's not valid so we're going with the default")
            else:
                print("Here we go!")
                self.Build_Map(int(input_rows), int(input_columns), 'def', 'def')
        else:
            print("That's not a valid input silly, try again!")
            self.Map_Input()
    
    def Check_Start_End(self, start, end, rows, columns):
        start = start.split(',')
        end = end.split(',')
        
        if start[0].isdigit() and start[1].isdigit():
            if int(start[0]) > 0 and int(start[0]) <= int(rows):
                if int(start[1]) > 0 and int(start[1]) <= int(columns):
                    if int(end[0]) > 0 and int(end[0]) <= int(rows):
                        if int(end[1]) > 0 and int(end[1]) <= int(columns):
                            return True
        else:
            return False
            
            
    def Check_Input(self, rows, columns):
# Function that checks if two inputs are non-zero, positive digits
        if rows.isdigit() and columns.isdigit():
            if int(rows) > 0 and int(columns) > 0:
                return True
            else:
                return False
        else:
            return False
    
    def Clean_Map(self):
# Function that will set all values in rows to '_'
        for i in list(range(0,len(self.Map))):
            for r in list(range(0,len(self.Map[0]))):
                self.Map[i][r] = '_'
    
    def Build_Map(self, rows, columns, start, end):
        
        self.Map = list(range(1,rows+1))
        
        for r in range(0, rows):
            self.Map[r] = list(range(1, columns)) 
        
        if start == 'def' and end == 'def':
            start = [1,1]
            end = [rows-1,columns-1]
        
        for i in range(1, len(start)):
            if start[i] == ',':
                start = start.split(',')
                break
        for i in range(1, len(end)):
            if end[i] == ',':
                end = end.split(',')
                break
        
        self.Map[int(start[0])-1][int(start[1])-1] = 'X'
        row = int(start[0])-1
        column = int(start[1])-1
        up = 0
        down = 1
        left = 2
        right = 3
        count = 0
        
        while self.Map[int(end[0])-1][int(end[1])-1] != 'X' and not count >= 200:
            count += 1
            direct = randint(0,4)     
            if direct == up:
                try:
                    row += 1
                    if self.Map[row][column] != 'X':
                        self.Map[row][column] = 'X'
                    else:
                        count -= 1
                except:
                    row -= 1
                    count -= 1
            elif direct == down:
                try:
                    row -= 1
                    if row >= 0:
                        if self.Map[row][column] != 'X':
                            self.Map[row][column] = 'X'
                        else:
                            count -= 1
                    else:
                        row += 1
                except:
                    row += 1
                    count -= 1
            elif direct == left:
                try:
                    column -= 1
                    if column >= 0:    
                        if self.Map[row][column] != 'X':
                            self.Map[row][column] = 'X'
                        else:
                            count -= 1
                    else:
                        column += 1
                except:
                    column += 1
                    count -= 1
            elif direct == right:
                try:
                    column += 1
                    if self.Map[row][column] != 'X':
                        self.Map[row][column] = 'X'
                    else:
                        count -= 1
                except:
                    column -= 1
                    count -= 1
#           print (str(row) + " " + str(column) + " " + str(count))
        if self.Map[int(end[0])-1][int(end[1])-1] == 'X':    
            for i in list(range(0, len(self.Map))):
                for r in list(range(0, len(self.Map[0]))):
                    rand = randint(0,1)
                    if self.Map[i][r] == 'X':
                        self.Map[i][r] = '_'
                    elif rand == 0:
                        self.Map[i][r] = '|'
                    elif rand == 1:
                        self.Map[i][r] = '|'
            self.Map[0][0] = '_'
            return
        
        self.Clean_Map()
        self.Build_Map(rows, columns, start, end)        
                
    def Print_Map(self):
        for r in self.Map:
            map_line = ""
            for i in r:
                map_line = str(map_line) + str(i)
            print(map_line)
                
chart = Map()

chart.Map_Input()

chart.Print_Map()