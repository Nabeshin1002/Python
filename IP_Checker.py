import subprocess
  
class IP(object):
    def __init__(self):
        self.IP = ""
        
    def IP_Valid(self):
        check = self.IP
        oct1 = ""
        oct2 = ""
        oct3 = ""
        oct4 = ""
        
        for n in check:
            if check == "":
                break
            elif n != ".":
                oct1 = oct1 + check[0]
                check = check[1:]
            elif n == ".":
                check = check[1:]
                for n2 in check:
                    if check == "":
                        break
                    elif n2 != ".":
                        oct2 = oct2 + check[0]
                        check = check[1:]
                    elif n2 == ".":
                        check = check[1:]
                        for n3 in check:
                            if check == "":
                                break
                            elif n3 != ".":
                                oct3 = oct3 + check[0]
                                check = check[1:]
                            elif n3 == ".":
                                check = check[1:]
                                for n4 in check:
                                    if n4 != ".":
                                        oct4 = oct4 + check[0]
                                        check = check[1:]
                                    else:
                                        print("oct4 ded")
                                        return False
                            else:
                                print("oct3 ded")
                                return False
                    else:
                        print("oct2 ded")
                        return False
            else:
                print("oct1 ded")
                return False
#        print(oct1 + " " + oct2 + " " + oct3 + " " + oct4)

        
        if  not oct1.isdigit() or (int(oct1) < 1 or int(oct1) > 255):
#            print("Oct1 sucks")
            return False
        elif not oct2.isdigit() or (int(oct2) < 0 or int(oct2) > 255):
#            print("Oct2 sucks more")
            return False
        elif not oct3.isdigit() or (int(oct3) < 0 or int(oct3) > 255):
#            print("Oct3 is bad and it should feel bad")
            return False
        elif not oct4.isdigit() or (int(oct4) < 0 or int(oct4) > 255):
#            print("Oct4 ruined an otherwise good thing")
            return False
        else:
            return True
    
    def IP_input(self):
        count = 3
        self.IP = input('Please enter a valid IP: ')
        if self.IP_Valid() == True:
            print("That is a valid IP, checking...")
            self.IP_Check()   
        while self.IP_Valid() == False:
            self.IP = input("That is not a valid IP, please try again: ")
            count -= 1
            if count == 0:
                print ("You suck at IP, bye")
                break
    
    def IP_Check(self):
        try:
            Test = subprocess.check_call("ping -n 1 {}".format(self.IP), stdout = subprocess.DEVNULL)
            print("Active")
        except:
            print("No response")

print("Welcome to Pingtester XP Super 2000!")

IP_run = IP()

IP_run.IP_input()