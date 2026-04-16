import pandas as pd
import numpy as np


def import_data(filepath):
    # Import URL dataset
    return pd.read_excel(filepath)

def clean_data(df):
    # Removing Missing and Null Values
    df.dropna(inplace=True)

    # Removing Duplicates
    df.drop_duplicates(inplace=True)

    # Binarizing the status column (phishing = 1, legitimate = 0)
    df['status'] = np.where(df['status'] == 'phishing', 1, 0)