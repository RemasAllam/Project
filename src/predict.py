import joblib
import pandas as pd
import numpy as np
import os

def predict_url(input_features, model_name='random_forest'):
    """
    Loads the saved scaler and model to predict a single URL's status.
    """
    model_file = f'trained models/{model_name.replace(" ", "_").lower()}.pkl'
    scaler_file = 'trained models/scaler.pkl'

    if not os.path.exists(model_file) or not os.path.exists(scaler_file):
        return "ERROR: Run main.py first"

    model = joblib.load(model_file)
    scaler = joblib.load(scaler_file)

    features_list = [
        'google_index', 'page_rank', 'nb_hyperlinks', 'web_traffic', 'domain_age', 
        'nb_www', 'phish_hints', 'ratio_intHyperlinks', 'longest_word_path', 
        'safe_anchor', 'ratio_extHyperlinks', 'ratio_digits_url', 'ratio_extRedirection', 
        'length_url', 'avg_word_path', 'char_repeat', 'length_hostname', 
        'shortest_word_host', 'length_words_raw', 'longest_words_raw'
    ]

    df_input = pd.DataFrame([input_features])[features_list]
    df_scaled = scaler.transform(df_input)

    prediction = model.predict(df_scaled)

    result = "PHISHING" if prediction[0] == 1 else "LEGITIMATE"
    return result

if __name__ == "__main__":
    sample_data =  {'google_index': 1, 'page_rank': 3, 'nb_hyperlinks': 15, 'web_traffic': 5000, 'domain_age': 400, 'nb_www': 1, 'phish_hints': 0, 'ratio_intHyperlinks': 0.8, 'longest_word_path': 10, 'safe_anchor': 50, 'ratio_extHyperlinks': 0.2, 'ratio_digits_url': 0.05, 'ratio_extRedirection': 0.0, 'length_url': 50, 'avg_word_path': 8, 'char_repeat': 0, 'length_hostname': 20, 'shortest_word_host': 4, 'length_words_raw': 12, 'longest_words_raw': 15}

    print("\n--- Running Single URL Prediction ---")
    label = predict_url(sample_data, model_name='random_forest')
    
    print(f"Result: {label}")