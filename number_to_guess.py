
print("Bienbenido al juego de adivinar un número entre el 0 y el 10")

tryes = 5

number_to_guess = 6

while tryes > 0:
    user_number = int(input("Numero: "))
    if user_number == number_to_guess:
        tryes = 0
        print("You Win")
    else:
        tryes -= 1
        print("Lo siento ese número no es, te quedan {} intentos".format(tryes))

if not user_number == number_to_guess:
    print("You Lose")
