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

# Test 3:  Does the prediction script load properly and returns a valid classification?
def test_prediction_logic():

    # Setup a sample input dictionary (must have the 20 features)
    sample_input = {
        'google_index': 1, 'page_rank': 3, 'nb_hyperlinks': 15, 'web_traffic': 5000,
        'domain_age': 400, 'nb_www': 1, 'phish_hints': 0, 'ratio_intHyperlinks': 0.8,
        'longest_word_path': 10, 'safe_anchor': 50, 'ratio_extHyperlinks': 0.2,
        'ratio_digits_url': 0.05, 'ratio_extRedirection': 0.0, 'length_url': 50,
        'avg_word_path': 8, 'char_repeat': 0, 'length_hostname': 20,
        'shortest_word_host': 4, 'length_words_raw': 12, 'longest_words_raw': 15
    }

    # Check if the required assets exist (requires main.py to have run once)
    model_exists = os.path.exists('trained models/random_forest.pkl')
    scaler_exists = os.path.exists('trained models/scaler.pkl')

    if not (model_exists and scaler_exists):
        pytest.skip("Skipping prediction test: Model or Scaler files not found. Run main.py first.")

    # Call the updated prediction function (now returns only the label)
    label = predict_url(sample_input, model_name='random_forest')

    # Assertions
    assert label in ["PHISHING", "LEGITIMATE"], f"Unexpected label returned: {label}"
    assert isinstance(label, str), "The returned result should be a string"

# Test 4: Does the main.py run from start to finish?
def test_main():
    csvpath = "Data/Processed Dataset.csv"

    results = main(csvpath)

    assert len(results) == 5
    assert 'XGBoost' in  results
    assert 0 <= results['Random Forest']['Accuracy'] <= 1

