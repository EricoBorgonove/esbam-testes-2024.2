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
        
        if 'erro' in dados_cep and not 'logradouro' in dados_cep:
            return {'erro': 'Cep não encontrado'}
        
        return dados_cep
    else:
        return {'erro': 'Não foi possível consultar o cep.'}