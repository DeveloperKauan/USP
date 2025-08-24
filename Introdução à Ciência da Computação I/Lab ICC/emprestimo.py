renda = float(input())
dividas = float(input())
valor_solicitado = float(input())

if renda <= 0:
    print("renda invalida")
else:
    indice_endividamento = dividas / renda

    if indice_endividamento > 1.0:
        print("negado")
    elif valor_solicitado > 20 * renda:
        print("negado")
    elif indice_endividamento >= 0.5:
        print("analise manual")
    else:
        if valor_solicitado <= 10 * renda:
            print("aprovado")
        else:
            print("analise manual")