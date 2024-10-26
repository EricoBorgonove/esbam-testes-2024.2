import pytest
from mediaAprovacao import calcularAprovacao 

@pytest.mark.parametrize('n1, n2, n3, expected', [
    (1,2,3, 'reprovado'),
    (5,5,5, "prova final"),
    (9,9,9, 'aprovado'), 
])

def test_calcularAprovacao_parametrizado(n1, n2, n3, expected):
    assert calcularAprovacao(n1, n2, n3) == expected

def test_calcularAprovacao ():
    with pytest.raises(ValueError, match="média incorreta"):
        calcularAprovacao (-1, -1, -1)
        calcularAprovacao (11, 11, 17)

    assert calcularAprovacao (10,10,10) == 'aprovado'
    assert calcularAprovacao (6,6,6) == 'prova final'
    assert calcularAprovacao (0,0,0) == 'reprovado'
    
    
    