
#TP 5 : MACHINE A LAVER

from math import ceil #Arrondir la valeur au supérieur
import time #gérer le temps

# Créer une classe qui va gérer la notion de lave linge
class LaveLinge:

    # Créer le constructeur
    def __init__(self, tours_minutes=1400, contenance_kg=8):
        self.tours_minutes = tours_minutes
        self.contenance_kg = contenance_kg
        self.contenance_actuelle_kg = 0
        self.temperature_actuel = 60
        self.duree_machine_defaut = 35
        self.duree_machine = 35
        print('Nouvelle machine ajoutée à la laverie')
        print('tours min: ', self.tours_minutes, 'contenance :', contenance_kg)

    # Méthodes
    def inserer_linge(self, poids_kg):
        print('Vous ouvrez la machine et vous entrez un total de ', poids_kg, 'kg')  

        # Vérification
        if poids_kg <= self.contenance_kg:
            print('OK ! le linge est à l\'interieur')
            self.contenance_actuelle_kg = poids_kg
        else:
            print('Ah non ! la machine est trop petite') 

    # Fonction demarrage de la machine
    def demarrage(self):

        # Vérifier si la machine est vide
        if self.contenance_actuelle_kg != 0:

            # Une boucle tant que la machine n'est pas à 0
            while self.duree_machine > 0:
                print(self.duree_machine,'s')
                self.duree_machine -= 1
                time.sleep(1) #Atteindre 1s

            # Afficher nombre de tours minutes
            print('Fin le compteur de tours minutes est:',35 * 1400)
        else:
            print('Démarrage impossible, vous n\'avez pas mis de linge')

    # Stopper la machine
    def stop(self):
        if self.duree_machine > 0:
            print('Arrêt ok !')
            self.duree_machine = 0
        else:
            print('Arrêt impossible, lave linge en cours d\'utilisation')    


#Afficher dans la console "Ouverture de la machine à laver"
print('Ouverture de la machine à laver')

#Appel de la fonction pour demarrer la machine
machine = LaveLinge(1200, 30) 

#Dictionnaire avec nos vêtements et leur poids
vetements = {
    "chemise_rouge_bleute":1,
    "manteau_de gravounai":6,
    "chaussette":4,
    "jean de yannis":18
}

total_kg = 0
for vetement in vetements.values():
    total_kg += vetement

print('Vous avez', total_kg, 'kg de vêtemnets')

#Nombre de machine que la personne va devoir effectuer
nbre_machine_a_effectuer = ceil((total_kg*2)/16)
print('Le nombre de machine à effectuer pour', total_kg, 'kg de linge est', nbre_machine_a_effectuer, 'machines')

#Calculer la consommation d'eau en L
quantite_eau = nbre_machine_a_effectuer * 60
print(f'La quantité d\'eau à utiliser pour {nbre_machine_a_effectuer} machines est {quantite_eau} L')

#Appeler la methode pour inserer le linge
machine.inserer_linge(total_kg)   

#Appeler la méthode pour demarrer la machine
machine.demarrage()

#Appeler la méthode pour stoper la machine
machine.stop()

