# fonction qui retourne la liste des nombres pairs entre deux nombres donnés

def return_even_numbers():

    # liste vide qui va contenir la liste des nombres pairs
    result = []
      

    # nombre minimal et maximal à entrer par l'utilisateur
    minimum = int(input("Entrez le minimum: "))
    maximum = int(input("Entrez le maximum: "))

    # vérifier si le maximum est un nombre (donc supérieur à 9)

    for i in range(minimum, maximum):
        if (i%2==0 and maximum > 9):
            result.append(i)
            # stocker le résultat sous forme d'une liste 
            strResult = result
            

        elif (i%2==0 and maximum < 9):
            # stocker le résultat sous forme d'une string qui est l'erreur à afficher 
            strResult = "Veuillez entrer une valeur maximale supérieure à 9"

    print(strResult)



return_even_numbers()



