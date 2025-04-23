import numpy as np
from model import train_model, predict

def test_model_training():
    """Test that model training works"""
    model_info = train_model()
    assert 'model' in model_info, "Model training should return a model"
    assert 'classes' in model_info, "Model training should return class names"

def test_model_prediction():
    """Test model predictions"""
    # Sample features for Iris setosa
    features = [5.1, 3.5, 1.4, 0.2]
    result = predict(features)
    
    # Check prediction format
    assert 'prediction' in result, "Prediction should contain a 'prediction' key"
    assert 'species' in result, "Prediction should contain a 'species' key"
    
    # Check prediction values
    assert isinstance(result['prediction'], int), "Prediction should be an integer"
    assert 0 <= result['prediction'] <= 2, "Prediction should be between 0 and 2"
    assert isinstance(result['species'], str), "Species should be a string"

if __name__ == "__main__":
    test_model_training()
    test_model_prediction()
    print("All tests passed!")
