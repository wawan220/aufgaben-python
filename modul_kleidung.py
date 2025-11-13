"""
1. schreibe eine Funktion namens 'Kleidung' die je nach eingegebener Temperatur 
    die Kleidung empfielt 
2. in dieser Funktion soll aber auch nach dem Niederschlag gefragt werden,  
    und sagen ob man einen Regenschirm braucht oder nicht
    
"""



def kleidung(temp):
    

    if temp>=25:
        print("Sommerkleidung reicht")
    elif temp>=15:
        print("jake empfohlen")
    else:
        print("zhie dich warm an")

    regen=input("Regnet es? (j/n) ")
    if regen.lower()=="j":
        print("nimm ein regenschirm mit")
    else:
        print("Du brauchst keinenn regenschirm")
    return regen

