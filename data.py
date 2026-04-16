import pandas as pd
from config import DATA_PATH

class DataProcessing():

    def __init__(self, n_samples=None):
        
        self.n_samples = n_samples

    def load_data(self):
        
        df = pd.read_csv(DATA_PATH)

        return df