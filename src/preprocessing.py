import pandas as pd
import numpy as np

# Import URL dataset
Dataset = pd.read_excel('C:/Users/remas/Documents/UNI/Level 4 Primers/Phishing Detector/Project/Data/Processed Dataset.xlsx')

df = pd.DataFrame(Dataset)

# Removing Missing and Null Values
df.dropna(inplace=True)

# Removing Duplicates
df.drop_duplicates(inplace=True)

# Binarizing the status column (phishing = 1, legitimate = 0)
df['status'] = np.where(df['status'] == 'phishing', 1, 0)