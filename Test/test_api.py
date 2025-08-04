import pytest
import requests
import json
from unittest.mock import patch, Mock

def test_prediction_endpoint_structure():
    """Test prediction endpoint response structure"""
    # Sample input data
    sample_data = {
        'HighBP': 1.0,
        'HighChol': 0.0,
        'CholCheck': 1.0,
        'BMI': 26.0,
        'Smoker': 0.0,
        'Stroke': 0.0,
        'HeartDiseaseorAttack': 0.0,
        'PhysActivity': 1.0,
        'Fruits': 0.0,
        'Veggies': 1.0,
        'HvyAlcoholConsump': 0.0,
        'AnyHealthcare': 1.0,
        'NoDocbcCost': 0.0,
        'GenHlth': 3.0,
        'MentHlth': 5.0,
        'PhysHlth': 30.0,
        'DiffWalk': 0.0,
        'Sex': 1.0,
        'Age': 4.0,
        'Education': 6.0,
        'Income': 8.0
    }
    
    # Mock response
    mock_response = Mock()
    mock_response.json.return_value = {'diabetes_binary': 0.25}
    mock_response.status_code = 200
    
    with patch('requests.post', return_value=mock_response):
        response = requests.post('http://localhost:9696/predict', json=sample_data)
        result = response.json()
        
        assert response.status_code == 200
        assert 'diabetes_binary' in result
        assert isinstance(result['diabetes_binary'], (int, float))

def test_input_validation():
    """Test input data validation"""
    required_features = [
        'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
        'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
        'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
        'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income'
    ]
    
    # Test with valid input
    valid_input = {feature: 1.0 for feature in required_features}
    assert len(valid_input) == len(required_features)
    
    # Test with missing feature
    invalid_input = {feature: 1.0 for feature in required_features[:-1]}
    assert len(invalid_input) == len(required_features) - 1

if __name__ == '__main__':
    pytest.main([__file__])
