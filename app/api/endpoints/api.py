from fastapi import APIRouter

from obj.starter import Starter
from obj.wine import Wine

router = APIRouter(prefix="/api", tags=["api"])

starter = Starter()

@router.post("/predict")
async def prediction(wine : Wine):
    """
    - Objectif : permet de réaliser une prédiction en donnant en body les données nécessaires du vin à celle-ci
    - Attention !! Il faut mettre une valeur pour quality et id même si celles-ci ne seront pas prises en compte dans la prédiction
    - Entrée : 
            wine : Caractéristiques du vin en body
    - Commentaires :
        Affiche la qualité prédite du vin entré en body
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    success, predicted_score = starter.prediction(wine)
    if success:
        return {"Prediction": predicted_score}
    else:
        return {"Error": "The wine cannot be predicted. Check if you fit your model before asking the prediction"}

@router.get("/predict")
async def bestWine():
    """
    - Objectif : Permet de générer une combinaison de données permettant d'identifier le “vin parfait” (probablement inexistant mais statistiquement possible)
    - Commentaires :
        Affiche les caractéristiques du vin parfait
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    return {"Best wine": starter.best_wine()}

@router.get("/model")
async def get_model():
    """
    - Objectif : Indique que le modèle a bien été sérialisé
    - Sortie : 
        - starter.model.model_file : nom du fichier du modèle sérialisé et son emplacement
    - Commentaires : Affiche un message avec le nom du fichier ainsi que sa localisation
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    result = starter.serialization()
    if result:
        return {"Message": "Model serialized in " + starter.model.model_file}
    else:
        return {"Error": "The model cannot be serialiazed"}

@router.get("/model/description")
async def descriptionModel():
    """
    - Objectif : Permet d'obtenir des informations sur le modèle
    - Attention ! Il faut avoir fait un retrain avant de tester cette fonction
    - Sortie :
        params : paramètres du modèle généré,
        predicted_score : précision du modèle,
        descriptionY : description de la varible quality du dataset
    - Commentaires : Affiche les paramètres en sortie
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    success, params, predicted_score, descriptionY = starter.descriptionModel()
    if success:
        return {"Parameters": params, "Predicted score on the test dataset": predicted_score, "Description of the target variable": descriptionY}
    else:
        return {"Error": "The model cannot be described. Check if you fit your model before asking its description"}

@router.put("/model")
async def add_to_csv(wine : Wine):
    """
    - Objectif : Met à jour le fichier csv en y ajoutant un nouveau vin et ses caractéristiques
    - Entrée :
        wine : Caractéristiques du vin
    - Commentaires : 
        L'id entré ne sera pris en compte et sera remplacé par un id unique lors de l'écriture dans le fichier,
        Affiche un message de confirmation d'ajout au csv
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    if starter.add_to_csv(wine):
        return {"Message": "Wine added to Wines.csv"}
    else:
        return {"Error": "Please fill in the quality field with a value between 1 and 10 (included)"}

@router.post("/model/retrain")
async def retrain():
    """
    - Objectif : Entraîne un modèle
    - Commentaires : Affiche un message de confirmation de l'entrainement du modèle
    - Auteurs : Axel BOURRAS & Augustin NESSON
    """
    starter.retrain()
    return {"Message": "Model trained successfully"}
