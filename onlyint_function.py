
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
