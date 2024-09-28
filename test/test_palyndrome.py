import  python.src.palyndrome as p

def test_good():
    assert p.ispalyndrome("") == True
    assert p.ispalyndrome("a") == True
    assert p.ispalyndrome("aba") == True
    assert p.ispalyndrome("aA") == True
    assert p.ispalyndrome(" a a") == True
    assert p.ispalyndrome("abccba") == True
   
def test_bad():
    assert p.ispalyndrome("ab") == False
    assert p.ispalyndrome("abc") == False
    assert p.ispalyndrome("abcdba") == False

    
       
    