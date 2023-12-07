import random

numerovezes = input("Quantos jogos queres fazer?")
numerovezes = int(numerovezes)

ch = 0
cc = 0

while numerovezes > 0:
    numerovezes = numerovezes - 1

    jogadaHumana = input("Qual a tua jogada?")
    jogadaComputador = random.choice(["Rock", "Paper", "Scissors"])
    print(f"a jogada do computador foi:{jogadaComputador}")

    if jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "rock":
        print("empate \n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "scissors":
        print("ganhaste\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "paper":
        print("perdeste\n")
        ch += 0
        cc += 1


    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "paper":
        print("empate\n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "rock":
        print("ganhaste\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "paper":
        print("perdeste\n")
        ch += 0
        cc += 1


    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "paper":
        print("ganhaste\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "scissors":
        print("empate\n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "rock":
        print("perdeste\n")
        ch += 0
        cc += 1

print(f"O computador ganhou {cc} vezes, tu ganhaste {ch} vezes.")