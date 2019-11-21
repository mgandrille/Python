#programme pour vérifier si une année est bissextile

#demande année
annee=input("saisissez une année : ")
annee=int(annee)

bissextile = False

#programme
if annee %400 == 0:
    bissextile = True
elif annee %100 == 0:
    bissextile = False 
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile :
    print(annee, "est une année bissextile")
else:
    print(annee, "n'est pas une année bissextile")
