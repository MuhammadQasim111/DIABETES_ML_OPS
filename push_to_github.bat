@echo off
REM GitHub Repository Push Script for Diabetes ML Project (Windows)
REM Repository: https://github.com/MuhammadQasim111/DIABETES_ML_OPS

echo 🚀 Setting up Git repository for Diabetes ML Project...
echo Repository: https://github.com/MuhammadQasim111/DIABETES_ML_OPS
echo ============================================================

REM Initialize git repository if not already initialized
if not exist ".git" (
    echo 📁 Initializing Git repository...
    git init
) else (
    echo ✅ Git repository already initialized
)

REM Add remote origin
echo 🔗 Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/MuhammadQasim111/DIABETES_ML_OPS.git

REM Create .gitignore file
echo 📝 Creating .gitignore file...
(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo build/
echo develop-eggs/
echo dist/
echo downloads/
echo eggs/
echo .eggs/
echo lib/
echo lib64/
echo parts/
echo sdist/
echo var/
echo wheels/
echo pip-wheel-metadata/
echo share/python-wheels/
echo *.egg-info/
echo .installed.cfg
echo *.egg
echo MANIFEST
echo.
echo # Virtual Environment
echo .env
echo .venv
echo env/
echo venv/
echo ENV/
echo env.bak/
echo venv.bak/
echo.
echo # Jupyter Notebook
echo .ipynb_checkpoints
echo.
echo # MLflow
echo mlruns/
echo diabetes_mlflow.db
echo.
echo # Models (large files)
echo *.pkl
echo *.joblib
echo *.h5
echo *.model
echo models/*.lgb
echo models/*.txt
echo.
echo # Data files (can be large)
echo datasets/*.csv
echo datasets/*.zip
echo datasets/*.parquet
echo.
echo # CatBoost info
echo catboost_info/
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo *~
echo.
echo # OS
echo .DS_Store
echo .DS_Store?
echo ._*
echo .Spotlight-V100
echo .Trashes
echo ehthumbs.db
echo Thumbs.db
echo.
echo # Logs
echo *.log
echo logs/
echo.
echo # Temporary files
echo *.tmp
echo *.temp
echo .cache/
echo.
echo # Docker
echo *.dockerignore
echo.
echo # Environment variables (keep template, ignore actual values)
echo .env.local
echo .env.production
echo.
echo # Monitoring
echo grafana_data/
echo prometheus_data/
) > .gitignore

echo ✅ .gitignore created

REM Stage all files
echo 📦 Staging files for commit...
git add .

REM Create initial commit
echo 💾 Creating initial commit...
git commit -m "Initial commit: Complete Diabetes ML Project" -m "" -m "Features:" -m "- MLflow experiment tracking and model registry" -m "- Prefect workflow orchestration" -m "- Flask API deployment with Docker support" -m "- Model monitoring with Evidently, Prometheus, Grafana" -m "- Comprehensive testing suite" -m "- Complete MLOps pipeline" -m "" -m "Project Structure:" -m "- Model Training and Tracking (MLflow)" -m "- Workflow Orchestration (Prefect)" -m "- Model Deployment (Flask + Docker)" -m "- Model Monitoring (Evidently + Grafana)" -m "- Testing and Documentation" -m "" -m "Technologies: Python, MLflow, Prefect, Flask, Docker, LightGBM, XGBoost, CatBoost"

REM Push to GitHub
echo 🌐 Pushing to GitHub repository...
git branch -M main
git push -u origin main

echo.
echo 🎉 Successfully pushed to GitHub!
echo Repository URL: https://github.com/MuhammadQasim111/DIABETES_ML_OPS
echo.
echo Next steps:
echo 1. Visit your repository on GitHub
echo 2. Add repository description and topics
echo 3. Download datasets as mentioned in GETTING_STARTED.md
echo 4. Set up your local environment and start experimenting!

pause
