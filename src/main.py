from palyndrome import ispalyndrome

print("let`s detect a palyndrome!")
entry = input('Please enter the word to test for palyndrome:')
print("the word {0} is {1}a palyndrome".format(entry,("" if ispalyndrome(entry) else "not ")))