from  src.palyndrome import ispalyndrome

def test_good():
    """
    Test good palyndrome
    """
    assert ispalyndrome("") == True
    assert ispalyndrome("a") == True
    assert ispalyndrome("aba") == True
    assert ispalyndrome("aA") == True
    assert ispalyndrome(" a a") == True
    assert ispalyndrome("abccba") == True
   
def test_bad():
    """
    Test bad palyndrome
    """
    assert ispalyndrome("ab") == False
    assert ispalyndrome("abc") == False
    assert ispalyndrome("abcdba") == False

    
       
    