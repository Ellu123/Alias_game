import random #Importerar modulen random


file = open("alias_ord", 'r', encoding = "UTF-8") #Tar orden från text filen och gör den till en lista
lines = file.readlines()
list_word = []
for l in lines:
    if l == "\n": #Kollar ifall det finns några tomma rader. If == True, struntar den i den och bara börjar på nästa
        pass
    else:
        l = l.replace("\n", "")
        list_word.append(l.split(", "))


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
print("Vill du börja? (j för ja eller n för nej)") #Input för att börja programmet
svar = input("> ").upper()

if svar == "Y" or svar == "YES" or svar == "J" or svar == "JA":
    svar = True

else:
    print("Är du säker att du vill avsluta programmet? (j för ja eller n för nej)") #Kollar om du verkligen vill avsluta programmet eller om du bara tryckte fel knapp
    svar = input("> ").upper()

    if svar == "N" or svar == "NO" or svar == "NEJ":
        svar = True
    else:
        svar = False


while svar == True:
    alias_ord_random = random.choice(list_word) #Tar en anv orden från listan
    alias_ord_finslipning = "".join(alias_ord_random) #Gör så att när man printar ut ordet ser det inte hemskt ut
    print()
    print()
    print(alias_ord_finslipning)
    print()
    print()
    list_word.remove(alias_ord_random) #Tar bort ordet från listan så att den inte kan användas igen

    if len(list_word) == 0: #Kollar ifall det finns några ord kvar, if = true meddelar spelet och slutar
        print()
        print("Du har använt alla ord")
        print("Stäng programmet och öppna på nytt ifall du vill köra igen")
        break

    print()
    print("Nästa ord? (j för ja eller n för nej)") #Frågar att printa ut nästa ord så att den inte printar ut alla ord på en gång
    svar = input("> ").upper()
    if svar == "Y" or svar == "YES" or svar == "J" or svar == "JA":
        svar = True

    else:
        print("Är du säker att du vill avsluta programmet? (j för ja eller n för nej)")
        svar = input("> ").upper()

        if svar == "N" or svar == "NO" or svar == "NEJ":
            svar = True
        else:
            svar = False

input()















