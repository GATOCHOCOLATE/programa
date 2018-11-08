
print("Bienbenido al juego de adivinar un número entre el 0 y el 10")

attempts = 5

number_to_guess = 6

user_number = None

while attempts > 0:
    user_number = int(input("Numero: "))
    if user_number == number_to_guess:
        attempts = 0
        print("You Win")
    else:
        attempts -= 1
        print("Lo siento ese número no es, te quedan {} intentos".format(attempts))

if not user_number == number_to_guess:
    print("You Lose")
