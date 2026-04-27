import sys
import os
import pytest
import pandas as pd
import numpy as np
from src.preprocessing import preprocessing
from src.main import main
from src.predict import predict_url

# Test 1: Does the file open?
def test_file_loading():
    csvpath = "Data/Processed Dataset.csv"
    assert os.path.exists(csvpath), f'Dataset {csvpath} not found!'

    df = pd.read_csv(csvpath)
    assert not df.empty

    assert 'status' in df.columns

# Test 2: Does phishing turn into 1 and legitimate turn into 0 in the status column?
def test_binarization():

    # Test it with a small dataset
    
    Features =  ['google_index', 'page_rank', 'nb_hyperlinks', 'web_traffic', 'domain_age', 'nb_www', 'phish_hints', 'ratio_intHyperlinks', 'longest_word_path', 'safe_anchor', 'ratio_extHyperlinks', 'ratio_digits_url', 'ratio_extRedirection', 'length_url', 'avg_word_path', 'char_repeat', 'length_hostname', 'shortest_word_host', 'length_words_raw', 'longest_words_raw']
    
    Data = {col: np.random.rand(40) for col in Features}

    Data['url'] = ['http://sample-url.com'] * 40
    Data['status'] = ['phishing'] * 20 + ['legitimate'] * 20
    Data['nb_com'] = [1] * 40
    Data['https_token'] = [0] * 40
    Data['nb_www'] = [5] * 40

    df = pd.DataFrame(Data)


    X_train, X_val, X_test, Y_train, Y_val, Y_test = preprocessing(df)

    assert X_train['nb_www'].max() == 1

    assert Y_train.iloc[0] in [0, 1]

    assert all(col in X_train.columns for col in Features)




