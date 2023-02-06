nev = input("Adja meg a jegyzetelendő fájl nevét! ")
fajl = open(nev,"w")

while True:
    jegyzet = input("Új sor: ")
    if jegyzet =="stop":
        break
    fajl.write(f"{jegyzet}\n")
fajl.close()