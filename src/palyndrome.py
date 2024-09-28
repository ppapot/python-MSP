import string



def ispalyndrome(entry) : 
    cleanEntry = entry.upper().replace(' ','')
    length = len(cleanEntry)
    for i in range(round(length/2)):
        if cleanEntry[i] != cleanEntry[length-(i)-1] :
            return False
    return True


print("let`s detect a palyndrome!")
entry = input('Please enter the word to test for palyndrome:')
print("the word {0} is {1}a palyndrome".format(entry,("" if ispalyndrome(entry) else "not ")))