def calcularAprovacao (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media < 0 or media >10:
        raise ValueError("média incorreta")
    elif media >=0 and media < 5:
        return "reprovado"
    elif media >= 5 and media < 7:
        return "prova final"
    elif media >=7 and media <= 10:
        return "aprovado"

        