import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    """Train a simple model on the Iris dataset and return it"""
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Calculate accuracy
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Save model info for predictions
    model_info = {
        'model': model,
        'classes': iris.target_names
    }
    
    # Save the model to disk
    with open('model.pkl', 'wb') as f:
        pickle.dump(model_info, f)
    
    return model_info

def load_model():
    """Load the trained model from disk"""
    try:
        with open('model.pkl', 'rb') as f:
            model_info = pickle.load(f)
        return model_info
    except FileNotFoundError:
        print("Model file not found, training a new model...")
        return train_model()

def predict(features):
    """Make a prediction with the trained model"""
    model_info = load_model()
    model = model_info['model']
    classes = model_info['classes']
    
    # Ensure features is a 2D array
    if isinstance(features, list):
        features = np.array(features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)[0]
    species = classes[prediction]
    
    return {
        "prediction": int(prediction),
        "species": str(species)
    }

if __name__ == "__main__":
    # Train and save the model
    train_model()
    print("Model trained and saved successfully!")
