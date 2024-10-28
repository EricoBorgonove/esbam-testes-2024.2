

#  pytest -v  --- testa todos os arquivos
# pytest -v -k  arquivo testa somente o "arquivo"

import requests
from via_cep_2 import consulta_cep

def test_consulta_cep_():
    cep = '69040230'
    resultado = consulta_cep(cep)
    
    assert 'erro' not in resultado
    assert resultado['cep'] == "69040-230"
    assert resultado["logradouro"] == "Rua Angelim"
    assert resultado["localidade"] == "Manaus"
    assert resultado["uf"] == "AM"
