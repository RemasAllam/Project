from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve, f1_score
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd


def evaluation(trained_models, X_test, Y_test):

    final_metrics_table = []
    final_metrics = {}

    plt.figure(figsize=(10, 7))
    plt.plot([0, 1], [0, 1], 'k--', label='Baseline (Random)')


    for name, model in trained_models.items():
        # Test the Model
        Y_pred = model.predict(X_test)

        # Probabilities Calculation for ROC-AUC
        if hasattr(model, "predict_proba"):
            Y_prob = model.predict_proba(X_test) [:, 1]

        else:
            Y_prob = model.decision_function(X_test)

        # Calculate the Accuracy & Metrics
        matrix = confusion_matrix(Y_test, Y_pred)
        acc = accuracy_score(Y_test, Y_pred)
        auc = roc_auc_score(Y_test, Y_prob)
        f1 = f1_score(Y_test, Y_pred)
        
        final_metrics[name] = {
            "Accuracy": acc,
            "Confusion Matrix": confusion_matrix(Y_test, Y_pred),
            "Classification Report": classification_report(Y_test, Y_pred, target_names=['Legitimate', 'Phishing']),
            "AUC": auc
        }


        final_metrics_table.append({
            "Model": name,
            "Accuracy": f"{acc:.4f}",
            "ROC-AUC": f"{auc:.4f}",
            "F1-Score": f"{f1:.4f}"
        })

        # Visualization for ROC Curve
        fpr, tpr, _ = roc_curve(Y_test, Y_prob)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {auc:.2f})')

        # Print Results
        print(f"Model: {name}")
        print(f"ROC-AUC: {auc:4f}\n")
        print(f"Confusion Matric: \n{matrix}\n")

    # Plot and save the ROC Curve 
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves - Phishing Detection Models')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    plt.savefig('ROC Curves Comparison.png') 
    plt.close() 
    
    print("\nROC Curve visualization saved as 'ROC Curves Comparison.png'")

    # Print the comparison table
    df_results = pd.DataFrame(final_metrics_table)
    print("\n" + "="*60)
    print("                MODEL COMPARISON SUMMARY")
    print("="*60)
    print(df_results.to_string(index=False))
    print("="*60 + "\n")

    return final_metrics

# Defining the Important Features
def feature_importance(model, features, model_name):
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = np.argsort(importances)[-10:]
        
        # Visualization of Feature Engineering
        plt.figure(figsize=(10, 6))
        plt.title(f'Top 10 Feature Importances - {model_name}')
        plt.barh(range(len(indices)), importances[indices], align='center')
        plt.yticks(range(len(indices)), [features[i] for i in indices])
        plt.xlabel('Relative Importance')
        plt.tight_layout()
        plt.savefig(f'Feature Importance {model_name}.png')
        print(f"Feature importance plot saved for {model_name}")

# Statistical Sigificance Test
def calculate_statistical_significance(model_a_scores, model_b_scores, name_a, name_b):

    t_stat, p_value = stats.ttest_rel(model_a_scores, model_b_scores)
    
    print(f"\n--- Statistical Significance: {name_a} vs {name_b} ---")
    print(f"P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Result: The difference is statistically significant (p < 0.05).")
    else:
        print("Result: The difference is NOT statistically significant.")