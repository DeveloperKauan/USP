peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

if imc < 18.5:
    print("magreza")
elif imc < 25:
    print("normal")
elif imc < 30:
    print("sobrepeso")
elif imc < 40:
    print("obesidade")
else:
    print("obesidade grave")