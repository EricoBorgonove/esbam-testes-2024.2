


import requests

def consulta_cep (cep):
    #fazer a requisição para a API do Via Cep
    
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get (url)
    print (response.status_code)
    
    #Verificar se o http status code == 200
    
    
    if response.status_code == 200:
        #convertendo a resposta pata o json e retornando os dados
        dados_cep = response.json()
        return dados_cep
    else:
        return {'erro': 'Não foi possível consultar o cep.'}
    
#Exemplo de consulta ao cep: 69045420
    
cep_usuario = input("Digite um cep: ")

dados = consulta_cep (cep_usuario)
print(dados)
