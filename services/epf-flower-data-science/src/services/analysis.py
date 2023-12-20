import json
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd
from src.services.data import split_dataset  # Importing the split_dataset function

def train_model(test_size):
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
