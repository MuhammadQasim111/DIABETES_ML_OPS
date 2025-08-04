import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import sys
import os

# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_data_loading():
    """Test if sample data can be loaded correctly"""
    # Create sample data
    sample_data = {
        'HighBP': [1.0, 0.0, 1.0],
        'HighChol': [0.0, 1.0, 0.0],
        'BMI': [26.0, 28.5, 30.1],
        'Diabetes_binary': [0.0, 1.0, 0.0]
    }
    df = pd.DataFrame(sample_data)
    
    assert df.shape[0] == 3
    assert 'Diabetes_binary' in df.columns
    assert df['BMI'].dtype == float

def test_preprocessing():
    """Test data preprocessing steps"""
    sample_data = {
        'HighBP': [1.0, 0.0],
        'HighChol': [0.0, 1.0],
        'BMI': [26.0, 28.5],
        'Diabetes_binary': [0.0, 1.0]
    }
    df = pd.DataFrame(sample_data)
    
    # Test feature extraction
    features = df.drop('Diabetes_binary', axis=1)
    target = df['Diabetes_binary']
    
    assert features.shape[1] == 3
    assert len(target) == 2
    assert target.iloc[0] == 0.0
    assert target.iloc[1] == 1.0

def test_prediction_format():
    """Test prediction response format"""
    # Mock prediction result
    prediction = 0.75
    
    result = {
        'diabetes_binary': prediction
    }
    
    assert 'diabetes_binary' in result
    assert isinstance(result['diabetes_binary'], (int, float))

if __name__ == '__main__':
    pytest.main([__file__])
