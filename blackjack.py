
import random 

# pole do ktorého budeme ukladať hodnoty
kartydealera=[]
kartyhráča=[]

# Funkcia sa bude vykonávať do vtedy až.....
# až kým dlzka kariet dealera bude rovný 2
while len(kartydealera)!=2:
    kartydealera.append(random.randint(1,11))
    if len(kartydealera)==2:
        print("Dealer má X &", kartydealera[1])
# až kým dlzka kariet hráča bude rovný 2
while len(kartyhráča)!=2:
    kartyhráča.append(random.randint(1,11))
    if len(kartyhráča)==2:
        print("Máš: ", kartyhráča)

# Dealer-hodnota kariet spolu
if sum(kartydealera)==21:
    print("Dealer má 21 a vyhráva ")
elif sum (kartydealera)>21:
    print("Dealer je v háji")

# Hráč -hodnota kariet menšia než 21
while sum(kartyhráča)<21:
    potiahnut=str(input("Chceš si potiahnuť ešte jednu ? (Ano/Nie) "))
    if potiahnut=="Ano":
        kartyhráča.append(random.randint(1,11))
        print("Teraz máš celkovo spolu: " + str(sum(kartyhráča))+ "",kartyhráča)
    else:
        print("Dealer má celkovo " + str(sum(kartydealera))+ "s", kartydealera)
        print("Hráč má celkovo " + str(sum(kartyhráča))+ "s",  kartyhráča)
        if sum(kartydealera)>sum(kartyhráča):
            print("Dealer vyhral !! ")
        else:
            print("Vyhral si !!")
            break
# Hráč- hodnota kariet väčšia nez 21
if sum(kartyhráča)>21:
    print("Prehral si, Dealer vyhral ")

# Hráč- hodonota kariet rovná=21
if sum(kartyhráča)==21:
    print("Máš BLACKJACK! Vyhral si ")

