contagem = 0
lancamentos = 0

while contagem != 3:
    linha = input()
    numero = int(linha)

    if 1 <= numero <= 6:
        lancamentos += 1

        if numero == 6:
            contagem += 1
        else:
            contagem = 0

    else:
        print("Numero invalido! Digite um numero entre 1 e 6.")

print(f"Voce conseguiu 3 seis consecutivos em {lancamentos} lancamentos!")