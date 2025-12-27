import pandas as pd

def add_features(df):
    """Creates new columns for analysis."""
    # Family Size
    if 'sibsp' in df.columns and 'parch' in df.columns:
        df['family_size'] = df['sibsp'] + df['parch'] + 1
    
    # Is Alone
    if 'family_size' in df.columns:
        df['is_alone'] = (df['family_size'] == 1).astype(int)
        
    # Title Extraction (Note the 'r' for raw string to fix the syntax warning)
    if 'name' in df.columns:
        df['title'] = df['name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
        df['title'] = df['title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 
                                         'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
        df['title'] = df['title'].replace('Mlle', 'Miss').replace('Ms', 'Miss').replace('Mme', 'Mrs')
        
    return df