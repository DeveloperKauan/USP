numero = 1
maior = 0
while numero != 0:
    if maior < numero:
        maior = numero
    numero = int(input())
print(maior)