import random

def onlyint(question, n_min, n_max):

    number = True

    while number < n_min or number > n_max or number == True:
        while True:
            try:
                number = int(input(question))
                break
            except:
                print("That's not a valid option!")
        if number < n_min or number > n_max:
            print("That's not a valid option!")
    return number


print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
print("Bienbenido al juego de adivinar un número entre el 0 y el 10")
print("-------------------------------------------------------------")

attempts = onlyint("Antes de nada debes elegir el numero máximo de intentos (entre 1 y 6): ", 1, 6)

game_mode = input("¿Qué modo de juego quieres jugar? (S)singleplayer (M)nultiplayer : ").upper()

user_number = None

while game_mode != "S" and game_mode != "M":
    game_mode = input("Vuelve a introducir el modo de juego: ").upper()

if game_mode == "S":

    number_to_guess = random.randint(0, 10)

    while attempts > 0:
        user_number = int(input("El número es: "))
        if user_number == number_to_guess:
            attempts = 0
            print("You Win")

        elif user_number == "":
            user_number = int(input("Introduce un número porfavor :"))

        else:
            attempts -= 1
            print("Lo siento ese número no es, te quedan {} intentos".format(attempts))


    if not user_number == number_to_guess:
        print("You Lose")

else:

    print("Ahora el jugador que adivina no puede ver la pantalla")

    number_to_guess = onlyint("Introduzca el numero a adivinar (que su compañero no lo vea) : ", 0,10 )

    for repeat in range(200):
        print("Por favor introduzca un número del 0 al 10 : {} ".format(random.randint(0,10)))

    print("Es el turno del jugador que adivina")

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
