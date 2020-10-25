keyLength = 5

#The key which permutes the string. 
#1 goes to 3rd position, 2 to 1st position etc
mapping = [[1,3], [2,1], [3,4], [4,5], [5,2]]

def encrypt(keyLength_, mapArr, string):
    string = list(string)
    i = 0
    cipher = []
    while i<len(string):
        #Divide string in groups of characters of length keyLength_
        cipher.append(list(string[i:min(len(string), i+keyLength_)]))
        i+=keyLength_
    

    mapArr.sort(key=lambda x: x[0])

    #Append bogus character
    for i in range(abs(len(cipher[0]) - len(cipher[-1]))):
        cipher[-1].append('z')


    encrypted = []
    #Map the characters to new position based on the key
    for i, val in enumerate(cipher):
        encrypted.append([val[j[1]-1] for j in mapArr])
            

    return ''.join([j for i in encrypted for j in i])


def decrypt(keyLength_, mapArr, string):
    string = list(string)
    i = 0
    cipher = []
    while i<len(string):
        #Divide string in groups of characters of length keyLength_
        cipher.append(list(string[i:min(len(string), i+keyLength_)]))
        i+=keyLength_
    
    for i in range(abs(len(cipher[0]) - len(cipher[-1]))):
        cipher[-1].append('z')

    mapArr.sort(key=lambda x: x[-1])
    decrypted = []
    #Map the characters to original position based on the key
    for i, val in enumerate(cipher):
        decrypted.append([val[j[0]-1] for j in mapArr])
            

    return ''.join([j for i in decrypted for j in i])

