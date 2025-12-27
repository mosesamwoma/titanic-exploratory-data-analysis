import pandas as pd
from pathlib import Path

def load_data():
    """Finds the raw data file."""
    root = Path(__file__).parent.parent
    path = root / "data" / "raw" / "titanic.csv"
    
    if not path.exists():
        print(f"\n❌ FILE NOT FOUND: {path.absolute()}")
        raise FileNotFoundError()
        
    return pd.read_csv(path)

def clean_data(df):
    """Standardizes columns and handles nulls."""
    df.columns = [col.lower() for col in df.columns]
    
    if 'age' in df.columns:
        df['age'] = df['age'].fillna(df['age'].median())
    if 'embarked' in df.columns:
        df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    if 'fare' in df.columns:
        df['fare'] = df['fare'].fillna(df['fare'].median())
        
    return df