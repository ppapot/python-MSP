import string

def ispalyndrome(entry) : 
    cleanEntry = entry.upper().replace(' ','')
    length = len(cleanEntry)
    for i in range(round(length/2)):
        if cleanEntry[i] != cleanEntry[length-(i)-1] :
            return False
    return True


