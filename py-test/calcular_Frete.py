#1 Criar a Função:

#  Até 100 km: R$5,00 fixo mais R$0,10 por kg.
#  Entre 101 e 500 km: R$10,00 fixo mais R$0,20 por kg.
#  Acima de 500 km: R$20,00 fixo mais R$0,30 por kg.


def calculo_frete (distancia: int , peso: float) -> float:

    if distancia > 0 and distancia <= 100:
        tarifa = 5
        custo_peso = 0.1
    elif distancia >= 101 and distancia <= 500:
        tarifa = 10
        custo_peso = 0.2
    elif distancia >= 501:
        tarifa = 20
        custo_peso = 0.3
    else:
        raise ValueError("distância incorreta")
    return (tarifa * distancia + peso* custo_peso)


# 2 - Determinar as Classes de Equivalência

    # Classe 1 - distancia > 0 e distancia <= 100
    # Classe 2 - distancia >= 101 e distancia <= 500
    # Classe 3 - distancia >= 501 
    
# 3 - Análise do Valor Limite

#        1 - {-1 , 0 , 1 } {99, 100 , 101}
#        2 - {100, 101, 102} {499, 500, 501}
#        3 - {500, 501 , 502}  

    # Remoção dos Repetidos/Invalidos por Classe
    
#        1 - {-1 , 0 , 1 } {99, 100}
#        2 - {101, 102} {499, 500}
#        3 - {501 , 502}  

# 4 - Casos de Testes

# [
#     (-1, 1000, "distância incorreta"), inválido
#     (0, 1000, "distância incorreta"),  inválido
#     (1, 1000, 105),
#     (99, 1000,595),
#     (100, 1000, 600),
#     (101, 1000, 1210),
#     (102, 1000, 1220),
#     (499, 1000, 5190),
#     (500, 1000, 5200),
#     (501, 1000, 10320),
#     (502, 1000, 10340)
# ]
    
