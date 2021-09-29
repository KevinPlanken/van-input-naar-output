import math 

toegangsticket = input("Hoeveel toegangsticket: ")
VIPVRGameSeat1 = input("Hoeveel minuten VIPVRGameSeat: ")

totaal = ((745+(math.ceil(int(VIPVRGameSeat1)/5)*37))*int(toegangsticket))/100

#print("Totaal bedrag", totaal)

print("Dit geweldige dagje-uit met "+str(toegangsticket)+" mensen in de Speelhal met "+str(VIPVRGameSeat1)+" minuten VR kost je maar "+str(totaal)+" euro")
