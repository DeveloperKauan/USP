import random

s = int(input())
random.seed(s)

somaJogador = 0
somaBanco = 0
parouJogador = False

while True:
    # Definir nome e valor das cartas
    numsorteio = random.randint(1, 13)
    if numsorteio == 1:
        nomeCarta = "A"
        valorCarta = 1
    elif 2 <= numsorteio <= 10:
        nomeCarta = str(numsorteio)
        valorCarta = numsorteio
    elif numsorteio == 11:
        nomeCarta = "J"
        valorCarta = 10
    elif numsorteio == 12:
        nomeCarta = "Q"
        valorCarta = 10
    else: #Se o valor for 13
        nomeCarta = "K"
        valorCarta = 10

    somaJogador += valorCarta
    print(f"Você tirou {nomeCarta} (total {somaJogador})")

    if somaJogador > 21:
        print("Você estourou! Banco vence.")
        break #Parar o while true

    decisao = input().strip().lower() #Pra quando eu tava testando não me importar com espaço e letra maiuscula
    if decisao == "stand":
        parouJogador = True
        print("Você decidiu parar.")
        break
    elif decisao == "hit":
        continue

if not parouJogador or somaJogador > 21:
    pass
else: #Turno do banco, definir valor das cartas e ele parar com 17
    while somaBanco < 17:
        numsorteio = random.randint(1, 13)

        if numsorteio == 1:
            nomeCarta = "A"
            valorCarta = 1
        elif 2 <= numsorteio <= 10:
            nomeCarta = str(numsorteio)
            valorCarta = numsorteio
        elif numsorteio == 11:
            nomeCarta = "J"
            valorCarta = 10
        elif numsorteio == 12:
            nomeCarta = "Q"
            valorCarta = 10
        else:
            nomeCarta = "K"
            valorCarta = 10

        somaBanco += valorCarta
        print(f"Banco tirou {nomeCarta} (total {somaBanco})")

    if somaBanco > 21:
        print("Banco estourou! Você vence.")
    else:
        print("Banco parou.")
        print(f"Você: {somaJogador}, Banco: {somaBanco}")
        if somaJogador > somaBanco:
            print("Você venceu!")
        elif somaBanco > somaJogador:
            print("Banco venceu!")
        else:
            print("Empate!") #esculacho