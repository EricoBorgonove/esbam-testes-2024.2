import pytest
from soma import somar
from subtracao import subtrair
from multiplicacao import multiplicar
from divisao import dividir

def test_somar():
    assert somar(2,3) == 5
    assert somar(5,9) == 14
    assert somar(5,10) == 15
    assert somar(5,11) == 16
    assert somar(5,12) == 17
    assert somar(5,13) == 18
    assert somar(5,14) == 19
    assert somar(5,15) == 20
    
def test_subtrair ():
    assert subtrair(1,1) == 0
    assert subtrair(1, 7) == -6
    assert subtrair(9, 1) == 8
    
def test_multiplicar ():
    assert multiplicar(1,1) == 1
    assert multiplicar(10,7) == 70
    assert multiplicar(5,5) == 25
    assert multiplicar(9,3) == 27
    
def test_dividir ():
    with pytest.raises(ValueError, match="Não há divisão por 0"):
        dividir(10,0)
    assert dividir(1,1) == 1
    assert dividir(10,5) == 2