#!/bin/bash

# GitHub Repository Push Script for Diabetes ML Project
# Repository: https://github.com/MuhammadQasim111/DIABETES_ML_OPS

echo "🚀 Setting up Git repository for Diabetes ML Project..."
echo "Repository: https://github.com/MuhammadQasim111/DIABETES_ML_OPS"
echo "=" * 60

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add remote origin
echo "🔗 Adding remote repository..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/MuhammadQasim111/DIABETES_ML_OPS.git

# Create .gitignore file
echo "📝 Creating .gitignore file..."
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints

# MLflow
mlruns/
diabetes_mlflow.db

# Models (large files)
*.pkl
*.joblib
*.h5
*.model
models/*.lgb
models/*.txt

# Data files (can be large)
datasets/*.csv
datasets/*.zip
datasets/*.parquet

# CatBoost info
catboost_info/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp
.cache/

# Docker
*.dockerignore

# Environment variables (keep template, ignore actual values)
.env.local
.env.production

# Monitoring
grafana_data/
prometheus_data/
EOF

echo "✅ .gitignore created"

# Stage all files
echo "📦 Staging files for commit..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Complete Diabetes ML Project

Features:
- MLflow experiment tracking and model registry
- Prefect workflow orchestration
- Flask API deployment with Docker support
- Model monitoring with Evidently, Prometheus, Grafana
- Comprehensive testing suite
- Complete MLOps pipeline

Project Structure:
- Model Training and Tracking (MLflow)
- Workflow Orchestration (Prefect)
- Model Deployment (Flask + Docker)
- Model Monitoring (Evidently + Grafana)
- Testing and Documentation

Technologies: Python, MLflow, Prefect, Flask, Docker, LightGBM, XGBoost, CatBoost"

# Push to GitHub
echo "🌐 Pushing to GitHub repository..."
git branch -M main
git push -u origin main

echo ""
echo "🎉 Successfully pushed to GitHub!"
echo "Repository URL: https://github.com/MuhammadQasim111/DIABETES_ML_OPS"
echo ""
echo "Next steps:"
echo "1. Visit your repository on GitHub"
echo "2. Add repository description and topics"
echo "3. Download datasets as mentioned in GETTING_STARTED.md"
echo "4. Set up your local environment and start experimenting!"
