# 🩺 Diabetes Prediction ML Project - Getting Started

This is a comprehensive end-to-end machine learning project for diabetes prediction, covering the complete MLOps pipeline from experimentation to deployment and monitoring.

## 🎯 Project Overview

This project implements a diabetes prediction system using health indicators from the BRFSS 2015 dataset. It demonstrates:

- **Experiment Tracking** with MLflow
- **Workflow Orchestration** with Prefect  
- **Model Deployment** with Flask and Docker
- **Model Monitoring** with Evidently, Prometheus, and Grafana

## 📊 Dataset

The project uses the Diabetes Health Indicators Dataset from Kaggle:
- **Source**: [Kaggle - Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
- **Features**: 21 health indicator features (BMI, Blood Pressure, Cholesterol, etc.)
- **Target**: Binary diabetes prediction (0/1)
- **Size**: 70,692 records

## 🏗️ Project Structure

```
├── 1. Model Training and Tracking/     # MLflow experimentation
├── 2. Workflow Ochestration/           # Prefect workflows  
├── 3. Model Deployment/                # Flask API & Docker
├── 4. Model Monitoring/                # Evidently monitoring
├── datasets/                           # Data storage
├── models/                             # Trained models
├── Test/                               # Unit tests
└── requirements.txt                    # Dependencies
```

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Setup the project
python setup.py

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Datasets

Due to Kaggle's terms of service, download datasets manually:

1. Go to [Kaggle Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
2. Download these files to the `datasets/` folder:
   - `diabetes_012_health_indicators_BRFSS2015.csv.zip`
   - `diabetes_binary_5050split_health_indicators_BRFSS2015.csv.zip`

### 3. Model Training

```bash
cd "1. Model Training and Tracking"
jupyter notebook diabetes.ipynb
```

This notebook includes:
- Exploratory Data Analysis
- Multiple ML algorithms (LightGBM, XGBoost, CatBoost, Random Forest)
- Hyperparameter optimization
- MLflow experiment tracking

### 4. Workflow Orchestration

```bash
cd "2. Workflow Ochestration"
python model_training.py
```

### 5. Model Deployment

#### Local Deployment:
```bash
cd "3. Model Deployment"
python predict_local.py

# Test the API (in another terminal)
python test.py
```

#### Docker Deployment:
```bash
cd "3. Model Deployment"
docker build -t diabetes-prediction:v1 .
docker run -p 9696:9696 diabetes-prediction:v1
```

### 6. Model Monitoring

```bash
cd "4. Model Monitoring"
docker-compose up

# Send test data (in another terminal)
python send_data.py
```

Access monitoring dashboards:
- **Grafana**: http://localhost:3000
- **Prometheus**: http://localhost:9091

## 🔧 Configuration

### Environment Variables

Update `.env` file with your settings:

```bash
# AWS Configuration (if using cloud)
AWS_PROFILE=your_aws_profile
S3_BUCKET_NAME=your-bucket-name

# MLflow Configuration  
MLFLOW_TRACKING_URI=sqlite:///diabetes_mlflow.db
TRACKING_SERVER_HOST=localhost
```

### MLflow Setup

View experiments:
```bash
mlflow ui --backend-store-uri sqlite:///diabetes_mlflow.db
```

Navigate to http://localhost:5000 to see experiments.

## 📈 Model Performance

The best performing model achieves:
- **F1-Score**: ~0.76
- **Accuracy**: ~0.76
- **Algorithm**: LightGBM with optimized hyperparameters

## 🧪 Testing

Run tests:
```bash
cd Test
pytest test_*.py
```

## 🐳 Docker Support

The project includes Docker support for:
- Model deployment service
- Monitoring stack (Grafana, Prometheus, Evidently)

## 📚 Key Technologies

- **ML Libraries**: scikit-learn, LightGBM, XGBoost, CatBoost
- **Experiment Tracking**: MLflow
- **Orchestration**: Prefect
- **API**: Flask
- **Containerization**: Docker
- **Monitoring**: Evidently, Prometheus, Grafana
- **Testing**: pytest

## 🔄 MLOps Pipeline

1. **Data Ingestion**: Load and validate datasets
2. **Experimentation**: Compare models with MLflow tracking
3. **Training**: Automated training with Prefect workflows
4. **Deployment**: Containerized API service
5. **Monitoring**: Real-time model performance tracking
6. **Testing**: Comprehensive test coverage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request

## 📄 License

This project is for educational purposes as part of the MLOps Zoomcamp.

## 🆘 Troubleshooting

### Common Issues:

1. **Dataset not found**: Ensure datasets are downloaded to `datasets/` folder
2. **MLflow server not running**: Check if port 5000 is available
3. **Docker issues**: Ensure Docker daemon is running
4. **Import errors**: Verify all dependencies are installed

### Getting Help:

- Check individual README files in each directory
- Review error logs in terminal output
- Ensure all environment variables are set correctly

---

Happy Machine Learning! 🎉
