# Librerias
import pandas as pd
from data import DataProcessing

def main():

    ## Carga de datos
    data = DataProcessing()

    df = data.load_data()
    print(df.head())

    ## ML



if __name__ == "__main__":
    main()