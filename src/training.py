import joblib
from sklearn.model_selection import cross_val_score

def train_models(models, X_train, Y_train, X_val, Y_val, scaler):
    
    trained_models = {}
    cv_results = {}

    joblib.dump(scaler, 'trained models/scaler.pkl')

    for name, model in models.items():
        print(f'Training Model: {name}')

        # Collection of CV Results for the Statistical Significance Test
        scores = cross_val_score(model, X_train, Y_train, cv=5)
        cv_results[name] = scores

        if name == 'XGBoost':
            # Because XGBoost will stop training if there's no improvement
            model.fit(X_train, Y_train, eval_set=[(X_val, Y_val)], verbose = False)
        
        # Other models don't require special fitting
        else:
            model.fit(X_train, Y_train)
        
        trained_models[name] = model

        joblib.dump(model, f'trained models/{name.replace(" ", "_").lower()}.pkl')
        trained_models[name] = model

    return trained_models, cv_results