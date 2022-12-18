from dataclasses import dataclass

import os
import pandas as pd
import joblib
from pandas import Series
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

from obj.dataset import Dataset
from obj.wine import Wine

@dataclass
class Model:
    rf_model : RandomForestClassifier
    model_file : str

    def __init__(self, model_file : str) -> None:
        self.model_file = model_file        
        self.rf_model = RandomForestClassifier()

    def serialization(self):
        """
        - Objectif : Sérialise le modèle
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        try:
            joblib.dump(self.rf_model, self.model_file)
            return True
        except:
            return False

    def train(self, dataset : Dataset):
        """
        - Objectif : Entraine le modèle
        - Entrée : 
            dataset : Données splitées en base train et test pour le modèle
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        self.rf_model.fit(dataset.x_train, dataset.y_train)
        self.serialization()

    def load(self):
        """
        - Objectif : Charge le modèle sérialisé
        - Entrée : 
            dataset : Données splitées en base train et test pour le modèle
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        if os.path.isfile(self.model_file):
            self.rf_model = joblib.load(self.model_file)
    
    def prediction(self, wine : Wine):
        """
        - Objectif : permet de réaliser une prédiction en donnant en body les données nécessaires du vin à celle-ci
        - Attention !! Il faut mettre une valeur pour quality et id même si celles-ci ne seront pas prises en compte dans la prédiction
        - Entrée : 
                wine : Caractéristiques du vin en body
        - Sortie : Retourne la prédiction de la qualité du vin entré en body
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        self.load()
        try:
            predicted_score = self.rf_model.predict([[wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid, wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide, wine.total_sulfur_dioxide, wine.density, wine.pH, wine.sulphates, wine.alcohol]])
            return True, float(predicted_score[0])
        except:
            return False, 0.0

    def bestWine(self, df : DataFrame):
        """
        - Objectif : Permet de générer une combinaison de données permettant d'identifier le “vin parfait” (probablement inexistant mais statistiquement possible)
        - Entrée : 
            df : Dataframe du fichier csv
        - Sortie : Retourne les caractéristiques d'un vin parfait
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        df = df.drop('Id',axis=1)
        bestScore = df['quality'].max()
        df = df[df['quality']==bestScore]
        df = df.drop('quality',axis=1)
        return(df.mean())

    def descriptionModel(self, df : DataFrame, dataset : Dataset):
        """
        - Objectif : Permet d'obtenir des informations sur le modèle
        - Entrée : 
            df : Dataframe du fichier csv,
            dataset : Données splitées en base train et test pour le modèle
        - Sortie :
            params : paramètres du modèle généré,
            predicted_score : précision du modèle,
            descriptionY : description de la varible quality du dataset
        - Auteurs : Axel BOURRAS & Augustin NESSON
        """
        self.load()
        try:
            params = self.rf_model.get_params()
            predicted_score = self.rf_model.score(dataset.x_test, dataset.y_test)
            descriptionY = df["quality"].describe()

            return True, params, predicted_score, descriptionY
        except:
            return False, {}, 0.0, Series(dtype=float)