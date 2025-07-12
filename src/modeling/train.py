from pathlib import Path
from sklearn.model_selection import cross_validate, KFold
from sklearn.pipeline import Pipeline
from src.config import MODELS_DIR
import joblib
import numpy as np

def evaluate_model(preprocessor, model, X, y, cv_folds=5, random_state=42):
    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", model)
    ])

    cv = KFold(n_splits=cv_folds, shuffle=True, random_state=random_state)
    results = cross_validate(
        pipeline,
        X, y,
        scoring="neg_root_mean_squared_error",
        return_train_score=True,
        cv=cv
    )

    train_rmse = -results['train_score']
    val_rmse = -results['test_score']

    print("Training RMSE:", train_rmse)
    print("Validation RMSE:", val_rmse)
    print(f"Avg Train RMSE: {np.mean(train_rmse):.2f}")
    print(f"Avg Val RMSE: {np.mean(val_rmse):.2f}")
    print(f"Gap (Val - Train): {np.mean(val_rmse) - np.mean(train_rmse):.2f}")

    return pipeline, train_rmse, val_rmse

def save_model(pipeline, filename: str):
    path = MODELS_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, path)
    print(f"Model saved to {path}")




