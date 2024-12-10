import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data():
    """
    Loads the Iris dataset and returns it as a pandas DataFrame with species names.

    Returns:
        df (pd.DataFrame): Iris dataset with features and species names.
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    return df


def preprocess_data(df, test_size=0.2, random_state=42):
    """
    Preprocesses the data by splitting into training and testing sets and scaling features.

    Args:
        df (pd.DataFrame): The Iris dataset.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Controls the shuffling applied to the data before applying the split.

    Returns:
        X_train_scaled (np.ndarray): Scaled training features.
        X_test_scaled (np.ndarray): Scaled testing features.
        y_train (pd.Series): Training labels.
        y_test (pd.Series): Testing labels.
    """
    X = df.drop("species", axis=1)
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
