#Deris A Leon Carrillo
# I affirm that the code provided was created by only myself.

import socket

class Assignment2:
    # initilize the variables
    def __init__(self, year):
        self.year = year
    # Tells the age
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is ", age)
    #list the 10th aniversaries
    def listAniversaries(self):
        age = 2022 - self.year
        
        a = [ i for i in range(10, age, 10)]
        return a
    
    #modfues the year with the requested n int.
    def modifyYear(self, n):
        s1 = str(self.year)[:2]
        s1 = s1 * n
        
        s2 = ""
        for i in range(0, len(str(self.year)), 2):
            s2 += str(self.year*n)[i]
        
        return s1 + s2
    
    #checks wether the string is good
    @staticmethod
    def checkGoodString(string):
        digits = sum(c.isdigit() for c in string)
        if(len(string)<9 or not string[0].islower() or digits != 1):
            return False
        
        return True
    #stablishes a tcp connection
    @staticmethod
    def connectTcp(host, port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            target = (host, port)
            connection.connect(target)
            connection.close()
            return True
        except Exception as e:
            return False
        
    
        
    
    
