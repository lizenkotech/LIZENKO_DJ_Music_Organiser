leesmodus = "r"
toevoegmodus = "a"
schrijfmodus = "w"



print("Menu keuzen")
print("1. Nummer toevoegen")
print("2. Nummers bekijken")
print("3. Nummer zoeken")
print("4. Afsluiten")

keuzen = 0
while keuzen != 4:

    keuzen = int(input("maak je keuzen: "))

    if keuzen == 1:
        titel_nummer = input("Geef de titel van het nummer: ")
        artiest = input("Geef de naam van de artiest: ")
        muziekstijl = input("Geef de muziekstijl: ")

        tekstbestand = open("nummers.txt", "a")

        tekstbestand.write(titel_nummer + "\n")
        tekstbestand.write(artiest + "\n")
        tekstbestand.write(muziekstijl + "\n")
        tekstbestand.write("\n")

        tekstbestand.close()

        print("=== LIZENKO DJ MUZIEKBEHEER ===")
        print(f"Artiest: {artiest}")
        print(f"Muziekstijl: {muziekstijl}")
        print("=== INFORMATIE OVER HET NUMMER ===")
        print(f"Titel van het nummer: {titel_nummer}")
        print(f"Artiest: {artiest}")
        print(f"Muziekstijl: {muziekstijl}")


    elif keuzen == 2:
        print("Nummers bekijken")
        tekstbestand = open("nummers.txt", leesmodus)
        inhoud = tekstbestand.read()
        print(inhoud)
        tekstbestand.close()


    elif keuzen == 3:
        gezochte_titel = input("Welke titel wil je zoeken: ")

        tekstbestand = open("nummers.txt", leesmodus)
        inhoud = tekstbestand.read()
        tekstbestand.close()

        nummers = inhoud.strip().split("\n\n")
        nummer_gevonden = False

        for nummer in nummers:
            informatie = nummer.split("\n")

            if informatie[0].lower() == gezochte_titel.lower():
                print("")
                print("Nummer gevonden!")
                print("")
                print(f"Titel: {informatie[0]}")
                print(f"Artiest: {informatie[1]}")
                print(f"Muziekstijl: {informatie[2]}")
                print("")
                nummer_gevonden = True

        if nummer_gevonden == False:
            print("Nummer niet gevonden.")



    elif keuzen == 4:
        print("Afsluiten")
    else:
        print("ongeldig")




if keuzen == 1:

    titel_nummer = input("Geef de titel van het nummer: ")
    artiest = input("Geef de naam van de artiest: ")
    muziekstijl = input("Geef de muziekstijl: ")

    tekstbestand = open("nummers.txt", "a")

    tekstbestand.write(titel_nummer + "\n")
    tekstbestand.write(artiest + "\n")
    tekstbestand.write(muziekstijl + "\n")
    tekstbestand.write("\n")

    print("=== LIZENKO DJ MUZIEKBEHEER ===")
    print(f"Artiest: {artiest}")
    print(f"Muziekstijl: {muziekstijl}")
    print("=== INFORMATIE OVER HET NUMMER ===")
    print(f"Titel van het nummer: {titel_nummer}")
    print(f"Artiest: {artiest}")
    print(f"Muziekstijl: {muziekstijl}")