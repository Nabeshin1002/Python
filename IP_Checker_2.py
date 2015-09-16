import subprocess
  
class IP(object):
    def __init__(self):
        self.IP = ""
        file_write = False
           
    def IP_Valid(self):
# Checks to see if an IP is valid, returns True/False
        check = self.IP
        split_check = []
        oct1 = ""
        oct2 = ""
        oct3 = ""
        oct4 = ""
        
        split_check = check.split('.')
        
        if len(split_check) > 4:
            return False
        
        if len(split_check) < 4:
            return False
        
        oct1 = split_check[0]
        oct2 = split_check[1]
        oct3 = split_check[2]
        oct4 = split_check[3]
        
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
# Main function for inputing IPs and IP ranges/ Returns nothing
        print('This will check a single IP or range, please put * in any octet you wish to check a range for. Requires 4 octets total')
        write = input('Do you want to write a file Y/N: ')
        if write[0].lower() == 'y':
            self.file_write = True
        elif write[0].lower() == 'n':
            self.file_write = False
        else:
            print('I do not understand your input, file will not be written')
            self.file_write = False
        self.IP = input('Please enter a valid IP: ')
        if self.IP[0].lower() == 'e':
            return
        elif self.IP_Range_Valid() == True:
            if self.file_write:
                self.IP_File_Clean()
            print("Wildcard found, will check range of IPs")
            self.Range_Check()
        elif self.IP_Valid() == True:
            if self.file_write:
                self.IP_File_Clean()
            print("That is a valid IP, checking...")
            self.IP_Check()
        else:
            print("Invalid IP entered")
        print("")
        self.file_write = False
        self.IP_input()
            
    def IP_Range_Valid(self):
# Function for making sure that the wildcard is the only item in the 4th octet / Returns True /False
        check = self.IP
        oct1 = ""
        oct2 = ""
        oct3 = ""
        oct4 = ""
        index = 0
        
        for i in check:
            if i == '*':
                check_split = check.split('.')
        
                if len(check_split) < 4 or len(check_split) > 4:
                    return False
        
                if check_split[3] != '*':
                    return False
                
                oct1 = check_split[0]
                oct2 = check_split[1]
                oct3 = check_split[2]
                oct4 = check_split[3]
                
            
                if not oct1.isdigit() or (int(oct1) < 1 or int(oct1) > 255):
                    return False
                elif not oct2.isdigit() or (int(oct2) < 0 or int(oct2) > 255):
                    return False
                elif not oct3.isdigit() or (int(oct3) < 0 or int(oct3) > 255):
                    return False
                else:
                    return True
        else:
            return False
        
    def Range_Check(self):
# Function for checking all IPs within the wildcards range, prints results
        test = self.IP.split('.')
        
        for i in range(1,256):
            test[3] = i
            IP_ping = ""
            IP_ping = test[0] + "." + test[1] + "." + test[2] + "." + str(test[3])
            try:            
                ping_try = (subprocess.check_call("ping -n 1 {}".format(IP_ping), stdout = subprocess.DEVNULL))
                print("{} is active.".format(IP_ping))
                if self.file_write:                
                    self.IP_File(IP_ping, 1)
            except:
                print("No response from {}.".format(IP_ping))
                if self.file_write:                
                    self.IP_File(IP_ping, 0)
    
    def IP_Check(self):
# Pings a single IP to see if it is active
        try:
            Test = subprocess.check_call("ping -n 1 {}".format(self.IP), stdout = subprocess.DEVNULL)
            print("{} is active.".format(self.IP))
            if self.file_write:
                self.IP_File(self.IP, 1)
        except:
            print("No response from {}.".format(self.IP))
            if self.file_write:
                self.IP_File(self.IP, 0)
    
    def IP_File(self, IP, ping):
# Prints the IP ping check to file Pingtest.txt
        IP_Output = open("Pingtest.txt", "a")
        if ping == 1:
            IP_Output.write("IP: {} ".format(IP) + "Ping: Active\n")
            IP_Output.close()
        if ping == 0:
            IP_Output.write("IP: {} ".format(IP) + "Ping: No response\n")
            IP_Output.close()
        
    def IP_File_Clean(self):
        IP_Output = open("Pingtest.txt", "w")
        IP_Output.write("This is a ping test!\n")
        IP_Output.close()
        

print("Welcome to Pingtester XP Super 2000!")

IP_run = IP()

IP_run.IP_input()