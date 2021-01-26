import random  # Importerar modulen random


def FindFile():

    print("Vilken fil vill du använda?")
    textFile = input("> ")
    # Låter dig välja vilken fil du vill använda till spelet
    path = "./TextFiler/" + textFile + ".txt"
    while True:
        try:
            file = open(path, "r", encoding="UTF-8")
        except FileNotFoundError:                           # Kollar att filen finns
            print("Filnamnet hittades inte, försök igen.")
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
            # Tar orden från text filen och gör den till en lista
            l = l.replace("\n", "")
            list_word.append(l.split(", "))

    if list_word == []:  # Kollar ifall det finns ord i filen över huvudtaget. Om den saknar ord börjar funktionen på nytt
        print("Det finns inga ord i denna textfil, välj en annan.")
        print()
        FindFile()
    else:
        return list_word


def Game():

    svar = True
    list_word = FindFile()
    while svar == True:
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
        answ = input("> ").upper()

        if answ == "Y" or answ == "YES" or answ == "J" or answ == "JA" or answ == "":
            pass

        else:
            # Kollar om du verkligen vill avsluta programmet eller om du bara tryckte fel knapp
            print(
                "Är du säker att du vill avsluta programmet? (j för ja eller n för nej)")
            answ = input("> ").upper()

            if answ == "N" or answ == "NO" or answ == "NEJ":
                pass
            else:
                quit()

        random.shuffle(list_word)

        # Kör en for loop igenom alla ord (eller tills du vill sluta)
        for i in range(0, len(list_word)):

            print()
            print()
            print("".join(list_word[i]))
            print()
            print()

            print()
            if (i + 1) < len(list_word):
                # Frågar att printa ut nästa ord så att den inte printar ut alla ord på en gång
                print("Nästa ord? (j för ja eller n för nej)")
                answ = input("> ").upper()
                if answ == "N" or answ == "NO" or answ == "NEJ":
                    print(
                        "Är du säker att du vill avsluta programmet? (j för ja eller n för nej)")
                    answ = input("> ").upper()
                    if answ == "N" or answ == "NO" or answ == "NEJ":
                        pass
                    else:
                        quit()
            else:
                pass
        print()
        # Säger att du har använt alla ord och frågar om du vill spela igen
        print("Du har använt alla ord.")
        print("Vill du börja på nytt? (j el. n)")
        answ = input("> ").upper()
        if answ == "J" or answ == "Y" or answ == "JA" or answ == "YES":
            print()
            # Frågar om du vill använda samma ord eller om du vill använda en ny fil
            print("Vill du använda samma ord? (j el. n)")
            answ = input("> ").upper()
            # Börjar från att loggan printas (far inte till FindFile funktionen)
            if answ == "J" or answ == "Y" or answ == "JA" or answ == "YES":
                svar = True
            else:
                Game()  # Startar om hela Game funktionen
        else:
            print()
            print("Tack för att du spelade!")
            print()
            quit()


Game()
