#Works for strings consisting of alphabets only



def mulInv(a,m):
    """Computes modular multiplicative inverse
    a mod m"""
    t1 = 0
    t2 = 1
    n = m
    if m == 1: return 0
    while a>0:
        q = m//a
        r = m-q*a
        m = a
        a = r
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if m == 1:
        return t1 if t1>0 else n + t1
    else:
        return None


def encryptAffineCipher(mulKey, addKey, string):
    """Compute the cipher"""

    if mulInv(mulKey, 26)==None:
        return "Error: Improper key passed"
    string = string.upper()
    #Convert to letters with A at 0 position and so on
    zeroBaseConv = [ord(i) - ord('A') for i in string]
    #Convert to ciper
    ciphNum = [((i*mulKey)+addKey)%26 for i in zeroBaseConv]
    #Convert to ASCII representation
    encryptedChars = [chr(i+ord('A')) for i in ciphNum]
    return "".join(encryptedChars)


def decryptAffineCipher(mulKeyInv, addKeyInv, string):
    """Decrypt the cipher"""

    if mulInv(mulKeyInv, 26)==None:
        return "Error: Improper key passed"
    string = string.upper()
    #Convert to letters with A at 0 position and so on
    zeroBaseConv = [ord(i) - ord('A') for i in string]
    #Convert to ciper
    ciphNum = [((i+addKeyInv)*mulKeyInv)%26 for i in zeroBaseConv]
    #Convert to ASCII representation
    decryptedChars = [chr(i+ord('A')) for i in ciphNum]
    return "".join(decryptedChars)

