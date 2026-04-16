import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def split_data(df: pd.DataFrame):
    """Membagi data menjadi set pelatihan dan pengujian."""
    # Kolom target prediksi di dataset ini bernama 'cardio'
    X = df.drop(columns=["cardio"])
    y = df["cardio"]
    
    # 20% data test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series):
    """Melatih model Random Forest."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model