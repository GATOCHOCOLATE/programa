
print("Hola bienbenido al solucionador de problemas de selu")
user_name = input("¿Cómo te llamas?: ")

problem = input("Hola {} ¿Cual es tu problema?: ".format(user_name))

decision = input("vale, ¿Lo has buscado en google? (Si/No): ").upper()

answere = None

if decision == "NO":
    print("Abre tu navegador y busca {}".format(problem))
    answere = input("¿Lo has solucionado? (Si/No): ").upper()

elif decision == "SI":
    answere = input("¿Lo has solucionado? (Si/No): ").upper()

elif decision != "SI" or "NO":
    print("no se que has dicho, doy por hecho que has dicho: no. Sopregonao")
    print("Abre tu navegador y busca {}".format(problem))
    answere = input("¿Lo has solucionado? (Si/No): ").upper()

while answere != ("SI" or "NO"):
    print("Lo siento nose que has dicho ¿Puedes repetirmelo?")
    answere = str(input("¿Lo has solucionado? (Si/No): ").upper())

if answere == "SI":
    print("Genial hasta luego...")
elif answere == "NO":
    print("Llama a Jose luis el te ayudará")
