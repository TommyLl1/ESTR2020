import pandas as pd

def load_data():
    df = pd.read_csv("./DataSet4STAT/regression.csv")

    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    return X, y