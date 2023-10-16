#Programme qui demande l’âge et le sexe d’un habitant et affiche si il paient l'impot
s=input("Veuillez entrer votre sexe : ")
a=int(input("Veuillez entrer votre age : "))
if(s=="H" or s=="h" and a<=20 ):
    print("Paient l'impot")
elif(s=="F" or s=="f" and a>=18 and a<=35):
    print("Paient l'impot")
else:
    print("Ne paient pas l'impot")
