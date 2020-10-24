import math

#Write in columns and transmit row by row
fixedRow = 2

def encrypt(row, string):
    string = list(string)
    i = 0
    cipher = []
    #Append empty chars to make the array of chars evenly sized and easy to deal with
    for i in range(row - len(string)%row):
        string.append('')
    
    retCip = ''
    #Take the rows to transmit directly from the char array and combine
    for i in range(row):
        j = i
        while j<len(string):
            retCip+=string[j]
            j+=row

    return retCip

def decrypt(row, string):
    string = list(string)
    splits = math.ceil(len(string)/row)
    i = 0
    cipher = []
    #Append empty chars to make the array of chars evenly sized and easy to deal with
    for i in range(row - len(string)%row):
        string.append('')
    
    retCip = ''
    #Get the original message from the cipher
    for i in range(splits):
        j = i
        while j<len(string):
            retCip+=string[j]
            j+=splits

    return retCip
