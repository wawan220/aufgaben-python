"""
Schreibe ein kleines program das:
- vom benutzer eine Zahl als eingabe annimmt
- die zahl 4 gegen diese eingabe teilt
- es darf nicht zu einem error kommen wenn ein buchstabe verwendet wird
- es darf nicht zum absturz kommen wen die eingabe 0 ist
- weise den benutzer auf die fehler hin und ende das program 
- 
"""
import sys


try:
    x=int(input("gebe eine zahl ein: "))

    print(4/x)


#except(ZeroDivisionError,ValueError):
#    Print("gebe eine gültige ganzzahl ein")

except (ZeroDivisionError) :
    print("gebe eine gültige zahl ein, diese darf nicht 0 sein")
    print("es ist folgender fehler aufgetreten: ", sys.exc_info())

except (ValueError) :
    print("gebe eine gültige zahl ein, diese muss eine ganzzahl sein")
    print("es ist folgender fehler aufgetreten: ", sys.exc_info())

finally:
    print("starte das program bitte neu")

print("ende")