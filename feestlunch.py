
croissantjes = input("Hoeveel croissantjes: ")
stokbroden = input("Hoeveel stokbroden: ")
kortingsbonnen = input("Hoeveel kortingsbonnen: ")

totaal = ((int(croissantjes)*39)+(int(stokbroden)*278)-(int(kortingsbonnen)*50))/100

#print("Totaal bedrag", totaal)

print("De feestlunch kost je bij de bakker "+str(totaal)+" euro voor de "+str(croissantjes)+" croissantjes en de "+str(stokbroden)+" stokbroden als de "+str(kortingsbonnen)+" kortingsbonnen nog geldig zijn!")