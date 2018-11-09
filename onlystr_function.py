
def onlystr(question, str1, str2,):

    name = input(question)

    while name.upper() != str1 and name.upper() != str2:
        print("That's not a valid option!")
        name = input(question)

    return(name)


nombre = onlystr("Introduce tu nombre: ", "PACO", "PEPE")

print(nombre)
