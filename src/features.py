from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

def build_preprocessor(
        df: pd.DataFrame,
        target_cols:list,
        impute_strategy: str = "mean",
        scale: bool = True,
        cap_outliers: bool = False,
        power_transformer = True

):
      """
    Creates a ColumnTransformer preprocessing pipeline.

    Parameters:
    - df (pd.DataFrame): The dataset (with target columns)
    - target_cols (list): List of target column names
    - impute_strategy (str): 'mean' or 'median' for SimpleImputer
    - scale (bool): Whether to apply scaling (StandardScaler)
    - cap_outliers (bool): Whether to apply outlier capping

    Returns:
    - preprocessor (ColumnTransformer): sklearn-compatible pipeline
    - feature_names (list): list of numeric feature column names
    """
      feature_cols = df.select_dtypes(include=["int64", "float64"]).columns
      feature_cols = [col for col in feature_cols if col not in target_cols]

      steps =[]

      steps.append(('imputer', SimpleImputer(strategy=impute_strategy)))

      #cap outliers(optional)
      if cap_outliers:
            steps.append(('outlier_caping', OutlierCapper()))
      
      #transform
      if power_transformer:
            steps.append(('power', PowerTransformer(method='yeo-johnson')))    
      #scale
      if scale:
            steps.append(('scaler', StandardScaler()))      
      # numeric pipeline
      num_pipeline = Pipeline(steps=steps)

      processor =ColumnTransformer(
            transformers=[
                  ('num', num_pipeline, feature_cols)
            ]
      )
      return processor, feature_cols


class OutlierCapper(BaseEstimator, TransformerMixin):
    def __init__(self, multiplier=1.5):
        self.multiplier = multiplier
        self.bounds_ = {}

    def fit(self, X,y=None):
         X=pd.DataFrame(X)

         for col in X.columns:
              Q1 = X[col].quantile(0.25)
              Q3 = X[col].quantile(0.75)
              IQR = Q3 - Q1

              lower = Q1 - self.multiplier * IQR
              upper = Q3 + self.multiplier * IQR

              self.bounds_[col] = (lower, upper)

         return self   

    def transform(self, X):
         X = pd.DataFrame(X).copy()

         for col in X.columns:
              lower, upper = self.bounds_[col]
              X[col] = X[col].clip(lower, upper)

         return X     

    