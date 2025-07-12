import pandas as pd
from pathlib import Path

from .config import (
    RAW_DATA_DIR, 
    INTERIM_DATA_DIR, 
    PROCESSED_DATA_DIR, 
    EXTERNAL_DATA_DIR,
    logger
)

def load_data(filename: str, data_type:str = "raw") -> pd.DataFrame:
    data_dirs ={
        "raw": RAW_DATA_DIR,
        "interim": INTERIM_DATA_DIR,
        "processed": PROCESSED_DATA_DIR,
        "external": EXTERNAL_DATA_DIR
    }

    data_dir = data_dirs.get(data_type)
    if data_dir is None:
        raise ValueError(f"Invalid data_type: {data_type}. Must be one of: {list(data_dirs.keys())}")
    
    filepath = data_dir / filename
    logger.info(f"loading data from{filepath}")

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath)


def wrangle_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic data cleaning and wrangling."""
    df = df.copy()

    # drop high-cardilality categorical columns
    df.drop(columns=['PID'], inplace=True)

    # drop site because test set might be an entirely different site
    #keeping it would lead to a poor model
    df.drop(columns=['site'], inplace=True)

    #drop columns with multicolinearity
    df.drop(columns=['xhp20', 'mdem', 'lstn'], inplace=True)

    return df

def save_processed_data(df: pd.DataFrame, filename:str) -> None:
    filepath = PROCESSED_DATA_DIR / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)