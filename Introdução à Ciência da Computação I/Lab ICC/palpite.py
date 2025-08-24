##Eu quando nao leio e fico 40 minutos com o código certo e dando errado pq esqueci de definir a seed KKKKKKKKKKKKKKKKKKk

import random
semente = int(input())
random.seed(semente)
secret = random.randint(1,100)
chances = 7
palpite = None


while chances>0 :
    palpite = int(input())
    if palpite > secret:
        print("O número secreto é menor!")

    elif palpite < secret:
        print("O número secreto é maior!")
    
    elif palpite == secret:
        print("Parabéns! Você acertou!")
        break
        
    chances -= 1

if palpite!=secret:
    print(f"Suas 7 tentativas acabaram. O número secreto era {secret}.")