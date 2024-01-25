import random

numerovezes = input("How many games would you like to play? ")
numerovezes = int(numerovezes)

ch = 0
cc = 0

while numerovezes > 0:
    numerovezes = numerovezes - 1

    jogadaHumana = input("\nWhat's your move? ")
    jogadaComputador = random.choice(["Rock", "Paper", "Scissors"])
    print(f"\nThe computer play was: {jogadaComputador}")

    if jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "rock":
        print("It's a draw! \n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "scissors":
        print("You win!\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "rock" and jogadaComputador.lower() == "paper":
        print("You lose!\n")
        ch += 0
        cc += 1


    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "paper":
        print("It's a draw!\n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "rock":
        print("You win!\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "paper" and jogadaComputador.lower() == "paper":
        print("You lose!\n")
        ch += 0
        cc += 1


    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "paper":
        print("You win!\n")
        ch += 1
        cc += 0
    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "scissors":
        print("It's a draw!\n")
        ch += 0
        cc += 0
    elif jogadaHumana.lower() == "scissors" and jogadaComputador.lower() == "rock":
        print("You lose!\n")
        ch += 0
        cc += 1

print(f"The computer won {cc} times, You won! {ch} times.")