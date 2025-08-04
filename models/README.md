# Models Directory

This directory contains trained machine learning models for the diabetes prediction project.

## Contents:
- `model.lgb`: LightGBM model file for local deployment
- `best_model.pkl`: Best performing model (if using pickle format)
- MLflow artifacts and model registry information

## Model Information:
- **Algorithm**: LightGBM Classifier
- **Features**: 21 health indicator features
- **Target**: Binary diabetes prediction (0/1)
- **Performance**: F1-Score ~0.76, Accuracy ~0.76

## Usage:
The models in this directory are used by the prediction services in the deployment folder.
