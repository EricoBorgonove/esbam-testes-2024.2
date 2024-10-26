from subtracao import subtrair

def test_subtrair ():
    assert subtrair(1,1) == 0
    assert subtrair(1, 7) == -6
    assert subtrair(9, 1) == 8