import random  # Importerar modulen random


def FindFile():

    print("Vilken fil vill du använda?")
    textFile = input("> ")
    path = "./TextFiler/" + textFile + ".txt"
    # Tar orden från text filen och gör den till en lista
    # Låter dig välja vilken fil du vill använda till spelet
    while True:
        try:
            file = open(path, "r", encoding="UTF-8")
        except FileNotFoundError:                           # Kollar att filen finns
            print("Filnamnet hittades inte, försök igen")
            textFile = input("> ")
            path = "./TextFiler/" + textFile + ".txt"
        else:
            break

    lines = file.readlines()
    list_word = []
    for l in lines:
        if l == "\n":  # Kollar ifall det finns några tomma rader. If == True, struntar den i den och bara börjar på nästa
            pass
        else:
            l = l.replace("\n", "")
            list_word.append(l.split(", "))
    return list_word


def Game():

    list_word = FindFile()
    print()
    print()
    print(" ______________________________________________________________")
    print("(__   ____________________________________________________   __)")
    print("   | |             _        _____                _____    | |")
    print("   | |     /\     | |      |_   _|      /\      / ____|   | |")
    print("   | |    /  \    | |        | |       /  \    | (___     | |")
    print("   | |   / /\ \   | |        | |      / /\ \    \___ \    | |")
    print("   | |  / ____ \  | |____   _| |_    / ____ \   ____) |   | |")
    print("   | | /_/    \_\ |______| |_____|  /_/    \_\ |_____/    | |")
    print("   | |                                                    | |")
    print(" __| |_______________credits: Ella Rejström_______________| |__")
    print("(______________________________________________________________)")

    print()
    # Input för att börja programmet
    print("Vill du börja? (j för ja eller n för nej)")
    svar = input("> ").upper()

    if svar == "Y" or svar == "YES" or svar == "J" or svar == "JA":
        svar = True

    else:
        # Kollar om du verkligen vill avsluta programmet eller om du bara tryckte fel knapp
        print("Är du säker att du vill avsluta programmet? (j för ja eller n för nej)")
        svar = input("> ").upper()

        if svar == "N" or svar == "NO" or svar == "NEJ":
            svar = True
        else:
            svar = False

    while svar == True:
        # Tar en anv orden från listan
        random.shuffle(list_word)
        # Gör så att när man printar ut ordet ser det inte hemskt ut
        #alias_ord_finslipning = "".join(list_word)

        for i in range(0, len(list_word)):

            print()
            print()
            print("".join(list_word[i]))
            print()
            print()
            # Tar bort ordet från listan så att den inte kan användas igen

            print()
            # Frågar att printa ut nästa ord så att den inte printar ut alla ord på en gång
            print("Nästa ord? (j för ja eller n för nej)")
            svar = input("> ").upper()
            if svar == "Y" or svar == "YES" or svar == "J" or svar == "JA":
                svar = True

            else:
                print(
                    "Är du säker att du vill avsluta programmet? (j för ja eller n för nej)")
                svar = input("> ").upper()

                if svar == "N" or svar == "NO" or svar == "NEJ":
                    svar = True
                else:
                    svar = False
                    break
        print()
        print("Du har använt alla ord")
        print("Vill du börja på nytt?")
        svar = input("> ").upper()
        if svar == "J" or svar == "Y" or svar == "JA" or svar == "YES":
            print()
            print("Vill du använda samma ord?")
            svarFil = input("> ").upper
            if svarFil == "J" or svarFil == "Y" or svarFil == "JA" or svarFil == "YES":
                svar = True
            else:
                Game()


Game()
