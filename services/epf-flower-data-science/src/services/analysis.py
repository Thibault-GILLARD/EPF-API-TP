import json
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd
from src.services.data import split_dataset  # Importing the split_dataset function

def train_model(test_size):
    """Train and save a Logistic Regression model.

    Args:
        test_size (float): The ratio of test set to the whole dataset.

    Returns:
        dict: A dictionary containing the status of the training process or an error message.
    """
    try:
        # Load dataset
        dataset = pd.read_csv('src/data/Iris.csv')

        with open('services/epf-flower-data-science/src/config/model_parameters.json', 'r') as f:
            model_params = json.load(f)

        # Dropping 'Id' and using 'Species' as the target variable
        #X = dataset.drop(['Species'], axis=1)  # Drop 'Id' column
        #y = dataset['Species']  # Target variable

        X_train, X_test, y_train, y_test = split_dataset(test_size)

        model = LogisticRegression(**model_params)  

        # Train 
        model.fit(X_train, y_train)  

        # Save
        joblib.dump(model, 'src/data/trained_model.pkl')

        return {"status": "Model trained and saved successfully"}

    except Exception as e:
        return {"error": f"Error training model: {e}"}

def predict_flower(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    """Predict the flower species using the trained model.

    Args:
        SepalLengthCm (float): Length of sepal in centimeters.
        SepalWidthCm (float): Width of sepal in centimeters.
        PetalLengthCm (float): Length of petal in centimeters.
        PetalWidthCm (float): Width of petal in centimeters.

    Returns:
        dict: A dictionary containing the predicted flower species or an error message.
    """
    try:
        model = joblib.load('src/data/trained_model.pkl')
        prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
        return {"prediction": prediction[0]}

    except Exception as e:
        return {"error": f"Error predicting flower: {e}"}
    