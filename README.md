# Phishing URL Detection Pipeline

## Project Overview
This project implements a machine learning pipeline designed to detect phishing URLs by analyzing 20 specific features extracted from URL structures and web page content. The system evaluates multiple classifiers—including Random Forest, XGBoost, SVM, and Neural Networks—to determine the most effective model for malicious link detection.

## Installation & Setup
1. **Prerequisites**: Ensure Python 3.x is installed.
2. **Install Dependencies**: Use the provided requirements file to install necessary libraries:
   ```bash
   pip install -r requirements.txt

## Usage
### Running the Full Pipeline
To perform data preprocessing, feature scaling, model training, and comparative evaluation, run:
##### python -m src.main

### Individual URL Prediction
 To classify a single URL using a pre-trained model (default is Random Forest), use:
##### python -m src.predict

## API Function Documentation

## `preprocessing.py`
### `preprocessing(df)`
* **Parameters**: `df` (pandas.DataFrame) - The raw dataset.
* **Returns**: `X_train, X_val, X_test, Y_train, Y_val, Y_test` (numpy arrays).
* **Description**: Performs binarization on 20 features based on security red-flag thresholds and splits the data for training and validation.

## `feature_engineering.py`
### `top_20_features(X_train, X_val, X_test)`
* **Parameters**: Training, Validation, and Test feature sets.
* **Returns**: Scaled feature sets and the `StandardScaler` object.
* **Description**: Isolates the top 20 impactful features and applies standard scaling. Note: The scaler is fit only on the training set to prevent data leakage.

## `training.py`
### `train_models(models, X_train, Y_train, X_val, Y_val, scaler)`
* **Parameters**: Model dictionary, split data, and fitted scaler.
* **Returns**: `trained_models` (dict), `cv_results` (dict).
* **Description**: Handles the 5-fold cross-validation and final fitting of all algorithms. It also serializes the trained models as `.pkl` files.

## `evaluation.py`
### `evaluation(trained_models, X_test, Y_test)`
* **Parameters**: Dictionary of trained models and test data.
* **Returns**: `final metrics` (dict).
* **Description**: Calculates Accuracy, Precision, Recall, F1, and AUC. Generates and saves the 'ROC Curves Comparison.png' plot.

### `feature_importance(model, features, model_name)`
* **Parameters**: Trained model, list of feature names, and model name string.
* **Description**: Extracts feature importance scores (if available) and saves a horizontal bar chart as `Feature Importance [ModelName].png.`

### `calculate_statistical_significance(model_a_scores, model_b_scores, name_a, name_b)`
* **Parameters**: Arrays of cross-validation scores for two models.
* **Description**: Executes a Paired T-Test to determine if the performance difference is statistically significant ($p < 0.05$).

## `predict.py`
### `predict_url(input_features, model_name)`
* **Parameters**: `input_features` (dict), `model_name` (str).
* **Returns**: String ("PHISHING" or "LEGITIMATE").
* **Description**: Loads a saved model and scaler to classify a single URL based on provided feature values.