"""
erstelle eine Schleife die (einmalig) Überprüft
ob eine eingegebene Zahl Größer als 10 ist.
wenn die zahl größer ist soll ein entsprechender Text
ausgegeben werden und das gleiche wen die zahl 
kleiner als 10 ist oder wenn die zahl gleich 10 ist.
-----ERWEITERUNG----------------ERWEITERUNG---------
lasse diese überprüfung so oft durchlaufen, wie vom
Benutzer gewünscht, d.h. nach jeder überprüfung
abfragen ob eine weitere Zahl überprüft werden soll.
"""
run=True
while run==True:
    zahl=float(input("gib zahl: "))

    print("zahl größer 10" if zahl>10 else ("kleiner 10" if zahl<10 else "genau 10"))
    
    


    if zahl>10:
        print("zahl größer 10")
    elif zahl< 10:
        print("kleiner 10")
    else:
        print("genau 10")
    print("möchtest du noch eine uahl vergleichen? (j/n)")
    
    vergleich = input("> ")
    if vergleich == "n":
        run=False
    elif vergleich=="j":
        print("weitere zahl vergleiche: ")
    else:
        print("gebe j oder n ein: ")
    print("ende")



