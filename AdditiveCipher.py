#Works for strings consisting of alphabets only

def additiveCipherEncrypt(encryptionKey, string):
    string = string.upper()
    #Now 0 represents a, 1 represents b etc
    zeroBaseConv = [ord(i) - ord('A') for i in string]
    #'Shift' of shift cipher done on the string
    cipherNums = [(i+encryptionKey)%26 for i in zeroBaseConv]
    #Convert from 0 based representation to ASCII
    encryptedChars = [chr(i+ord('A')) for i in cipherNums]
    return "".join(encryptedChars)

def additiveCipherDecrypt(decryptionKey, string):
    if decryptionKey<0:
        #if instead of proper decryption key,
        #a negative of orginal key is given
        decryptionKey = decryptionKey + 26
 
    string = string.upper()
    #Now 0 represents a, 1 represents b etc
    zeroBaseConv = [ord(i) - ord('A') for i in string]
    #'Shift' the character for decryption
    cipherNums = [(i+decryptionKey)%26 for i in zeroBaseConv]
    #Convert from 0 based representation to ASCII
    decryptedChars = [chr(i+ord('A')) for i in cipherNums]
    return "".join(decryptedChars)
