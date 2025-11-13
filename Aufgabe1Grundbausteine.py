"""
1
gib in der konsole aus:
        das ist meine erste Aufgabe
        das ergebnis von 5+6 lautet 11

"""

print("das ist meine erste Aufgabe")
print("das ergebnis von 5+6 lautet", 5+6 ) 
print("das ergebnis von 5+6 lautet " + str(5+6) )
print(f"das ergebnis von 5+6 lautet {5+6}")



"""
2
der anwender soll zwei Zahlen 
über die konsole eingeben können 
und diese sollen mit eineander 
verrechnet werden:
    das ergebnis von a+b lautet c
"""
zahl1 = float(input("gebe zahl1: "))
zahl2 =float(input("gabe zahl2: "))
ergebnis=zahl1+zahl2
print(f"das ergebnis von {zahl1}+{zahl2} lautet {zahl1+zahl2}")
print("das ergebnis von ", zahl1 ,"+ ", zahl2, " lautet ", ergebnis)