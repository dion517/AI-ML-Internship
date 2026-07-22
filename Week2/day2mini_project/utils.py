import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)

    df["Total"] = df[["Mark1","Mark2","Mark3","Mark4","Mark5"]].sum(axis=1)
    df["Average"] = df["Total"] / 5

    return df