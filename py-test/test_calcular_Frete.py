import pytest
from calcular_Frete import calculo_frete

@pytest.mark.parametrize('distancia, peso, expected', [
    # (-1, 1000, "distância incorreta"),
    # (0, 1000, "distância incorreta"),
    (1, 1000, 105),
    (99, 1000,595),
    (100, 1000, 600),
    (101, 1000, 1210),
    (102, 1000, 1220),
    (499, 1000, 5190),
    (500, 1000, 5200),
    (501, 1000, 10320),
    (502, 1000, 10340)
])

def test_calcularFrete_parametrizado(distancia, peso, expected):
    assert calculo_frete(distancia, peso) == expected

def test_calcularFrete ():
    with pytest.raises(ValueError, match="distância incorreta"):
        calculo_frete(-1 , 1000)
        calculo_frete (0 , 1000)