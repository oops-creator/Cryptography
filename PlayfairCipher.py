key = 'LGDBAQMHECURNIFXVSOKZYWTP'


print('Key matrix is')
for i in range(0, len(key), 5):
    print(key[i:i+5])


def getRowCol(key, r,c):
    ind = r*5 + c
    return ind%25

def encryptPlayFair(enckey, string):
    string = string.upper()
    #Since J and I are same in this key we replace J with I
    string = string.replace('J', 'I')

    #insert bogus character for repeat character
    for s in range(0,len(string),2):
        if s<len(string)-1:
            if string[s]==string[s+1]:
                string=string[:s+1]+'X'+string[s+1:]

    #append bogus letter if odd number of terms
    if len(string)%2 != 0:
        string+='X'

    #Convert to ciper
    ciphNum = []
    for i in range(0,len(string), 2):
        index1 = enckey.find(string[i])
        row1 = index1//5
        col1 = index1%5
        index2 = enckey.find(string[i+1])
        row2 = index2//5
        col2 = index2%5


        if row1 == row2:
            first = enckey[getRowCol(key, row1, col1+1)]
            second = enckey[getRowCol(key, row2, col2+1)]
        elif col1 == col2:
            first = enckey[getRowCol(key, row1+1, col1)]
            second = enckey[getRowCol(key, row2+1, col2)]
        else:
            first = enckey[getRowCol(key, row1, col2)]
            second = enckey[getRowCol(key, row2, col1)]
        ciphNum.append(first)
        ciphNum.append(second)
    return "".join(ciphNum)

def decryptPlayFair(enckey, string):
    string = string.upper()
    #Since J and I are same in this key we replace J with I
    string = string.replace('J', 'I')
    #Convert to ciper
    ciphNum = []
    for i in range(0,len(string), 2):
        index1 = enckey.find(string[i])
        row1 = index1//5
        col1 = index1%5
        index2 = enckey.find(string[i+1])
        row2 = index2//5
        col2 = index2%5


        if row1 == row2:
            first = enckey[getRowCol(key, row1, col1-1)]
            second = enckey[getRowCol(key, row2, col2-1)]
        elif col1 == col2:
            first = enckey[getRowCol(key, row1-1, col1)]
            second = enckey[getRowCol(key, row2-1, col2)]
        else:
            first = enckey[getRowCol(key, row1, col2)]
            second = enckey[getRowCol(key, row2, col1)]
        ciphNum.append(first)
        ciphNum.append(second)
    
    ciphNum = "".join(ciphNum)

    #remove bogus letter if odd number of terms in original string
    if len(string)%2 != 0:
        string = string[:-1]
    #remove bogus character for repeat character
    for s in range(0,len(ciphNum)):
        if s<len(ciphNum)-2:
            if ciphNum[s]==ciphNum[s+2]:
                ciphNum=ciphNum[:s+1]+ciphNum[s+2:]

    return ciphNum

