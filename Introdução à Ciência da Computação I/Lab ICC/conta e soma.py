cont_positivos = 0
cont_negativos = 0
soma_positivos = 0.0
soma_negativos = 0.0

while True:
    try:
        numero = float(input())
        if numero == 0:
            break
        elif numero > 0:
            cont_positivos += 1
            soma_positivos += numero
        elif numero < 0:
            cont_negativos += 1
            soma_negativos += numero
    except EOFError:
        break

soma_total = soma_positivos + soma_negativos

print(f"Numero de valores positivos: {cont_positivos}")
print(f"Numero de valores negativos: {cont_negativos}")
print(f"Soma dos valores positivos: {soma_positivos:.1f}")
print(f"Soma dos valores negativos: {soma_negativos:.1f}")
print(f"Soma total: {soma_total:.1f}")