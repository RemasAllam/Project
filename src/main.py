import pandas as pd
from src.preprocessing import preprocessing
from src.feature_engineering import top_20_features
from src.models import models_definition
from src.training import train_models
from src.evaluation import evaluation, feature_importance, calculate_statistical_significance

def main(csvpath):
    print('---Starting Pipeline---')

    print(f'Loading Data from: {csvpath} ')
    df = pd.read_csv(csvpath)

    print('Cleaning, Binarizing, and Splitting Data...')
    X_train, X_val, X_test, Y_train, Y_val, Y_test = preprocessing(df)

    print('Defining the Top 20 Features and Scaling the Values...')
    X_train_scaled, X_val_scaled, X_test_scaled, scaler = top_20_features(X_train, X_val, X_test)
    
    features_list = ['google_index', 'page_rank', 'nb_hyperlinks', 'web_traffic', 'domain_age', 'nb_www', 'phish_hints', 'ratio_intHyperlinks', 'longest_word_path', 'safe_anchor', 'ratio_extHyperlinks', 'ratio_digits_url', 'ratio_extRedirection', 'length_url', 'avg_word_path', 'char_repeat', 'length_hostname', 'shortest_word_host', 'length_words_raw', 'longest_words_raw']
 

    print('Defining, Training, and Evaluating the Models...')
    model_def = models_definition()
    trained_models, cv_results = train_models(model_def, X_train_scaled, Y_train, X_val_scaled, Y_val, scaler)
    # Visualization of Feature Importance 
    if 'Random Forest' in trained_models:
            feature_importance(trained_models['Random Forest'], features_list, 'Random Forest')

    # Statistical Significance Test
    if 'Random Forest' in cv_results and 'XGBoost' in cv_results:
            calculate_statistical_significance(cv_results['Random Forest'], cv_results['XGBoost'], 'Random Forest', 'XGBoost')
    
    
    
    print("\n>>>>> FINAL RESULTS <<<<<\n")
    final_results = evaluation(trained_models, X_test_scaled, Y_test)

    print('---Pipeline Execution Complete---')
    return final_results

if __name__ == "__main__":
    Datapath = "Data/Processed Dataset.csv"

    try:
        main(Datapath)
    except FileNotFoundError:
        print(f"Error: Could not find '{Datapath}'. Please ensure the file is in the project root.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

