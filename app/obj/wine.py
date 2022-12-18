from dataclasses import dataclass

from pandas import DataFrame
from csv import writer

@dataclass
class Wine:
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: int
    total_sulfur_dioxide: int
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: int
    id: int

    def __init__(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality = -1, id = -1) -> None:
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = int(free_sulfur_dioxide)
        self.total_sulfur_dioxide = int(total_sulfur_dioxide)
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        # if quality == None:
        #     self.quality = quality
        # else:
        self.quality = int(quality)
        # self.id = None
        # if id == None:
        #     self.id = id
        # else:
        self.id = int(id)

    def add_to_csv(self, df : DataFrame, csv_file : str):
        """
        - Objectif : Met à jour le fichier csv en y ajoutant un nouveau vin et ses caractéristiques
        - Entrée :
            df : Dataframe du fichier csv
            csv_file : fichier csv à mettre à jour
        - Commentaires : 
            L'id entré ne sera pris en compte et sera remplacé par un id unique lors de l'écriture dans le fichier,
            Affiche un message de confirmation d'ajout au csv
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        if self.quality < 1 or self.quality > 10:
            return False
        # sys.exit("Please fill in the quality field of the wine you want to add to the csv file")
        idMax = max(df['Id'])
        newId = int(idMax) + 1
        self.id = newId

        with open(csv_file, 'a', newline='') as file:
            writer_object = writer(file)
            writer_object.writerow([self.fixed_acidity, self.volatile_acidity, self.citric_acid, self.residual_sugar, self.chlorides, self.free_sulfur_dioxide, self.total_sulfur_dioxide, self.density, self.pH, self.sulphates, self.alcohol, self.quality, self.id])
            file.close()

        return True