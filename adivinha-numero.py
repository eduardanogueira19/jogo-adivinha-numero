jogador1 = str(input("Nome do jogador 1: "))
jogador2 = str(input("Nome do jogador 2: "))
tentativas = 3
print("Vamos jogar?")
print("{} escolhe o número e o {} adivinha.".format(jogador1, jogador2))
Numero = int(input("{} escolha o número: ".format(jogador1)))
for tentativa in range(tentativas, 0, -1):
    print("{} tem {} tentativas!".format(jogador2, tentativa))
    numero = int(input("Adivinhe o número: \n"))
    if numero == Numero:
        print("Você acertou! Parabéns!")
        break
    else:
        if tentativa == 1:
            print("Acabaram as suas tentativas.")
            break
        print("Você errou! Tente novamente.")
