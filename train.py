# Librerias
import pandas as pd
from data import DataProcessing
from ml import ModelEvaluation

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def main():

    ## Carga de datos
    data = DataProcessing()

    X, y = data.load_xy()
    print(y.head())

    ## ML
    #model = LogisticRegression(max_iter=10000)
    model = DecisionTreeClassifier(max_depth=6)
    ml = ModelEvaluation(X=X, y=y)
    ml.eval(model=model)

if __name__ == "__main__":
    main()