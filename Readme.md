# Projet Wine Quality Prediction

## Par Axel BOURRAS et Augustin NESSON

## Présentation du projet

Le but de se projet est de créer et servir un modèle prédictif, qui donne une note sur la qualité d’un vin entré au modèle.

Pour la construction de ce projet, nous avons utilisé la bibliothèque FastAPI pour faire une API et des bibliothèques basées IA comme pandas ou scikit-learn pour construire nos fonctions

## Commandes à exécuter

Afin d'exécuter correcter le projet, il faut :
- Se placer dans à la racine du projet
- Ouvrir un terminal dans ce dossier puis faire :
   - `pip install -r requirements.txt` pour télécharger les packages nécessaires au fonctionnement du projet (conseil d'utilisation : exécuter cette commande dans un environnement virtuel)
   - `cd app/`
   - `uvicorn main:app --reload`
- Après avoir exécuté ces commandes aller à l'adresse http://127.0.0.1:8000/docs

Une présentation de l'API est visible sur http://127.0.0.1:8000
Pour une meilleure expérience visuelle cette l'aide (pour le voir sous forme JSON), vous pouvez utiliser Mozilla Firefox

## Contenu du projet

### Dataset

Nous avons utilisé le jeu de données Wines.csv présent dans le dossier static

Ce dataset contient les colonnes suivantes :

Input variables (based on physicochemical tests):
- fixed acidity | Acidité fixe : il s'agit de l'acidité naturelle du raisin comme l'acide malique ou l'acide tartrique.
- volatile acidity | Acidité volatile : l'acidité volatile d'un vin est constituée par la partie des acides gras comme l'acide acétique appartenant à la série des acides qui se trouvent dans le vin soit à l'état libre, soit à l'état salifié. L'acidité volatile donne au vin du bouquet.
- citric acid | Acide citrique : utilisé pour la prévention de la casse ferrique et participe au rééquilibrage de l'acidité des vins. 
- residual sugar | Sucre résiduel : sucres (glucose + fructose) encore présents dans le vin après fermentation.
- chlorides | Chlorures : matière minérale contenue naturellement dans le vin (sel, magnésium...)
- free sulfur dioxide | Sulfites libres : exhacerbent les propriétés antioxydantes du vin
- total sulfur dioxide | Sulfites libres + Sulfites liées à la réaction avec d'autres molécules du vin
- density | Densité du vin (g/l)
- pH | PH du vin
- sulphates | Sulfates : sels composés d'anions SO4(2-) != sulfites
- alcohol | degré d'alcool

Output variable (based on sensory data):
- quality | Qualité générale : note comprise en 0 et 10

### Analyse
Une étude du jeu de données est présente dans le dossier analyse, visible à la racine du projet. Elle est sous la forme d'un notebook .ipynb

### Fonctions

Les fonctions qui sont présentes dans ce projet sont :

- POST /api/predict permet de réaliser une prédiction en donnant en body les données nécessaires du vin à celle-ci

- GET /api/predict permet de générer une combinaison de données permettant d’identifier le “vin parfait” (probablement inexistant mais statistiquement possible)

- GET /api/model permet d’obtenir le modèle sérialisé

- GET /api/model/description permet d’obtenir des informations sur le modèle

- PUT /api/model permet d’enrichir le modèle d’une entrée de donnée supplémentaire (un vin en plus)

- POST /api/model/retrain permet de réentrainer le modèle

Des descriptions détaillées de chaque fonction sont disponibles à travers la docstring.

### Modèle

Pour la construction du modèle, nous avons choisi d'utiliser la méthode du Random Forest Classfier car c'est une méthode adéquate dans ce genre de problème et que nous n'avons pas trouvé d'autres techniques d'apprentissage plus performantes que celles-ci en termes de précision.

Quant aux hyperparamètres, nous en avons testé plusieurs en tentant de changer leurs valeurs mais les résultats obtenus étaient sensiblement les mêmes. Nous sommes donc restés sur notre premier choix qui était de garder les hyperparamètres par défaut.

Pour la sérialisation de celui-ci, nous avons utilisé la bibliothèque joblib qui permet d'enregistrer en modèle avec .dump et de le charger avec .load
