import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def top_20_features(X_train, X_val, X_test):
    # The top 20 features
    features = ['google_index', 'page_rank', 'nb_hyperlinks', 'web_traffic', 'domain_age', 'nb_www', 'phish_hints', 'ratio_intHyperlinks', 'longest_word_path', 'safe_anchor', 'ratio_extHyperlinks', 'ratio_digits_url', 'ratio_extRedirection', 'length_url', 'avg_word_path', 'char_repeat', 'length_hostname', 'shortest_word_host', 'length_words_raw', 'longest_words_raw']

    # Fit the Scaler on the Training Data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train[features])

    # Transform Validation and Test using the Train Scaler to Prevent Data Leakage
    X_val_scaled = scaler.transform(X_val[features])
    X_test_scaled = scaler.transform(X_test[features])

    return X_train_scaled, X_val_scaled, X_test_scaled, scaler 