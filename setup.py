#!/usr/bin/env python3
"""
Diabetes ML Project Setup Script
This script helps set up the environment and download necessary datasets.
"""

import os
import urllib.request
import zipfile
from pathlib import Path

def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        "datasets",
        "models", 
        "mlruns",
        "catboost_info",
        "Test",
        "1. Model Training and Tracking",
        "2. Workflow Ochestration", 
        "3. Model Deployment",
        "4. Model Monitoring"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")

def download_datasets():
    """Download diabetes datasets from Kaggle (requires manual download)"""
    print("\n📁 Dataset Setup:")
    print("Due to Kaggle's terms of service, datasets need to be downloaded manually.")
    print("Please follow these steps:")
    print("\n1. Go to: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset")
    print("2. Download the following files to the 'datasets' folder:")
    print("   - diabetes_012_health_indicators_BRFSS2015.csv.zip")
    print("   - diabetes_binary_5050split_health_indicators_BRFSS2015.csv.zip")
    print("\nNote: You may need a Kaggle account to download the datasets.")

def setup_mlflow():
    """Initialize MLflow setup"""
    print("\n🔬 MLflow Setup:")
    print("MLflow will use local SQLite database for tracking.")
    print("Run 'mlflow ui --backend-store-uri sqlite:///diabetes_mlflow.db' to view experiments.")

def setup_environment():
    """Setup Python environment"""
    print("\n🐍 Python Environment Setup:")
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n2. Or use pipenv:")
    print("   pipenv install")
    print("   pipenv shell")

def print_project_structure():
    """Print the project structure"""
    structure = """
📁 Project Structure:
├── 1. Model Training and Tracking/
│   ├── diabetes.ipynb          # Main ML experimentation notebook
│   └── README.md
├── 2. Workflow Ochestration/
│   ├── model_training.py       # Prefect workflow
│   └── README.md
├── 3. Model Deployment/
│   ├── predict_local.py        # Local model serving
│   ├── predict_remote.py       # Remote model serving
│   ├── test.py                 # API testing
│   ├── Dockerfile              # Container configuration
│   └── README.md
├── 4. Model Monitoring/
│   ├── send_data.py            # Data simulation
│   ├── docker-compose.yml      # Monitoring stack
│   └── README.md
├── datasets/
│   └── README.md               # Dataset information
├── models/
│   └── README.md               # Model storage
├── Test/
│   ├── test_data_processing.py # Unit tests
│   └── test_api.py             # API tests
├── requirements.txt            # Python dependencies
├── Pipfile                     # Pipenv configuration
├── .env                        # Environment variables
└── README.md                   # Main project README
"""
    print(structure)

def main():
    """Main setup function"""
    print("🚀 Setting up Diabetes ML Project...")
    print("=" * 50)
    
    create_directories()
    download_datasets()
    setup_mlflow()
    setup_environment()
    print_project_structure()
    
    print("\n✅ Setup complete!")
    print("Next steps:")
    print("1. Download the datasets as instructed above")
    print("2. Install Python dependencies: pip install -r requirements.txt") 
    print("3. Update .env file with your AWS credentials (if using AWS)")
    print("4. Start with the Jupyter notebook in '1. Model Training and Tracking'")

if __name__ == "__main__":
    main()
