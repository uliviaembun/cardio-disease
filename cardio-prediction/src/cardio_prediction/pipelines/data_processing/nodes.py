import pandas as pd

def preprocess_cardio(df: pd.DataFrame) -> pd.DataFrame:
    """Membersihkan data mentah kardiovaskular."""
    # age dari hari ke tahun
    df["age_years"] = (df["age"] / 365).round().astype(int)
    
    # BMI = berat(kg) / [tinggi(m)]^2
    df["bmi"] = df["weight"] / ((df["height"] / 100) ** 2)
    
    # drop irrelevant column
    return df.drop(columns=["id", "age"]) #