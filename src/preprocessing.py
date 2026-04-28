import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def import_data(filepath):
    # Import URL dataset
    return pd.read_csv(filepath)

def preprocessing(df):
    # Binarizing the Status Column (phishing = 1, legitimate = 0)
    df['status'] = np.where(df['status'] == 'phishing', 1, 0)

    # Binarization of Columns

    # Is the site indexed by Google?
    df['google_index'] = np.where(df['google_index'] == 0, 1, 0)

    # Page rank based on other sites.
    df['page_rank'] = np.where(df['page_rank'] <= 2, 1, 0)

    # Amount of time passed since the domain was registered.
    df['domain_age'] = np.where(df['domain_age'] < 180, 1, 0)

    # How many people visit the site?
    df['web_traffic'] = np.where(df['web_traffic'] > 150000, 1, 0)

    # Percentage of links that lead back to the same website.
    df['safe_anchor'] = np.where(df['safe_anchor'] < 30, 1, 0)

    # Sensitive word count.
    df['phish_hints'] = np.where(df['phish_hints'] > 0, 1, 0)

    # Ratio of internal links to the total number of links.
    df['ratio_intHyperlinks'] = np.where(df['ratio_intHyperlinks'] < 0.5, 1, 0)

    # Total number of links.
    df['nb_hyperlinks'] = np.where((df['nb_hyperlinks'] < 5) | (df['nb_hyperlinks'] > 100), 1, 0)

    # The full length of the URL
    df['length_url'] = np.where(df['length_url'] >= 75, 1, 0)

    # Does the URL have www?
    df['nb_www'] = np.where(df['nb_www'] != 1, 1, 0)

    # Percentage of numbers in the URL.
    df['ratio_digits_url'] = np.where(df['ratio_digits_url'] > 0.15, 1, 0)

    # Long hostname is a sign of phishing.
    df['length_hostname'] = np.where(df['length_hostname'] > 25 , 1, 0)

    # Longest string in the URL.
    df['longest_word_path'] = np.where(df['longest_word_path'] > 15, 1, 0)

    # Characters repeated more than two times is a sign of phishing.
    df['char_repeat'] = np.where(df['char_repeat'] >= 3, 1, 0)

    # Average length of words in the URL.
    df['avg_word_path'] = np.where(df['avg_word_path'] > 10, 1, 1)

    # Shortest word in the hostname.
    df['shortest_word_host'] = np.where(df['shortest_word_host'] <= 3, 1, 0)

    # Longest word, more than 30 characters is a sign of phishing.
    df['longest_words_raw'] = np.where(df['longest_words_raw'] > 20, 1, 0)

    # Measurement of word length accross the URL to identify abnormalities.
    df['length_words_raw'] = np.where(df['length_words_raw'] > 10, 1, 0)

    # Frequency of which a page redirects the user to external websites.
    df['ratio_extRedirection'] = np.where(df['ratio_extRedirection'] > 0 , 1, 0)

    # Ratio of external links to the total number of links.
    df['ratio_extHyperlinks'] = np.where(df['ratio_extHyperlinks'] > 0.5, 1, 0)


    # Identifying the variables
    X = df.drop(columns = ['url', 'status'])
    Y = df['status']

    # Split the 15% for testing
    X_rest, X_test, Y_rest, Y_test, = train_test_split(X, Y, test_size=0.15, random_state=42)

    #Split the 70% training and 15% validation
    X_train, X_val, Y_train, Y_val = train_test_split(X_rest, Y_rest, test_size=0.176, random_state=42)

    return X_train, X_val, X_test, Y_train, Y_val, Y_test