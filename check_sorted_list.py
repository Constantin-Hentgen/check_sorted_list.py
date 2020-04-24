liste = [0,1,2,3,4,100,5,6,7,8,9]
liste_clone = []

for z in range(0,len(liste)):
    liste_clone.append(liste[z])
temp = 0

for i in range(0, len(liste_clone)):
    for k in range(0, len(liste_clone)-1):
        if liste_clone[k] > liste_clone[k+1]:
            temp = liste_clone[k]
            liste_clone[k] = liste_clone[k+1]
            liste_clone[k+1] = temp

if liste_clone == liste:
    print('The original list is sorted')
else:
    print("The original list isn't sorted")
