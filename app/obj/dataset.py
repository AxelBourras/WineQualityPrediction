from dataclasses import dataclass

from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

@dataclass
class Dataset: 
    x_train : list
    x_test : list
    y_train : list
    y_test : list

    def __init__(self, df : DataFrame) -> None:
        x = df.drop('quality', axis=1)
        x = x.drop('Id', axis=1)
        y = df['quality']

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size = 0.3)
        scaling = StandardScaler()
        self.x_train = scaling.fit_transform(self.x_train)
        self.x_test = scaling.fit_transform(self.x_test)
