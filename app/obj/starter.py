from dataclasses import dataclass

from obj.wine import Wine
from obj.dataset import Dataset
from obj.model import Model
from obj.dataframeRooter import DataframeRooter

@dataclass
class Starter: # toutes les fonctions pour les apis
    model_file : str
    csv_file : str
    df_rooter : DataframeRooter
    dataset : Dataset
    model : Model

    def __init__(self, model_file = "saved_model/model.joblib", csv_file = "static/Wines.csv") -> None:
        self.model_file = model_file
        self.csv_file = csv_file
        self.df_rooter = DataframeRooter(self.csv_file)
        self.df = self.df_rooter.get_dataframe()
        self.dataset = Dataset(self.df)
        self.model = Model(model_file)

        self.model.load()

    def prediction(self, wine : Wine):
        return self.model.prediction(wine)

    def best_wine(self):
        return self.model.bestWine(self.df)

    def serialization(self):
        return self.model.serialization()

    def descriptionModel(self):
        return self.model.descriptionModel(self.df, self.dataset)

    def add_to_csv(self, wine : Wine):
        result = wine.add_to_csv(self.df, self.csv_file)
        if result:
            self.df_rooter = DataframeRooter(self.csv_file)
            self.df = self.df_rooter.get_dataframe()
            self.dataset = Dataset(self.df)
            self.model = Model(self.model_file)
        
        return result

    def retrain(self):
        self.model.train(self.dataset)