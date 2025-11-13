"""
Lagere deine Funktion Kleidung aus, so das man sie hier verwenden kann.
"""

import modul_kleidung



mk=modul_kleidung

temperatur=float(input("wie viel grad sind es draußen? "))
#kleidung(temperatur)
unwetter=mk.kleidung(temperatur)
print(unwetter)
