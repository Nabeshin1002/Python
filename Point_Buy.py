def create_char_pb():
    pb = 27
    pb_cost = {8 : 0, 9 : 1, 10 : 2, 11 : 3, 12 : 4, 13 : 5, 14 : 7, 15 : 9}
    attribute = ['Strength', 'Dexterity', 'Consitution', 'Intelligence', 'Wisdom', 'Charisma']
    
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
        print(attribute[i])
        
create_char_pb()