# GitHub Setup Guide for Diabetes ML Project

## Quick Setup Commands

### Option 1: Using the Automated Script (Recommended)

For **Windows PowerShell/Command Prompt**:
```cmd
cd c:\MLOPS
.\push_to_github.bat
```

For **Git Bash or WSL**:
```bash
cd /c/MLOPS
./push_to_github.sh
```

### Option 2: Manual Git Commands

If you prefer to run commands manually:

```bash
# Navigate to project directory
cd c:\MLOPS

# Initialize Git repository
git init

# Add remote repository
git remote add origin https://github.com/MuhammadQasim111/DIABETES_ML_OPS.git

# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: Complete Diabetes ML Project

Features:
- MLflow experiment tracking and model registry
- Prefect workflow orchestration  
- Flask API deployment with Docker support
- Model monitoring with Evidently, Prometheus, Grafana
- Comprehensive testing suite
- Complete MLOps pipeline

Technologies: Python, MLflow, Prefect, Flask, Docker, LightGBM, XGBoost, CatBoost"

# Set main branch and push
git branch -M main
git push -u origin main
```

## Repository Structure Being Pushed

```
DIABETES_ML_OPS/
├── 1. Model Training and Tracking/
│   ├── diabetes.ipynb                 # Main ML experimentation notebook
│   └── README.md
├── 2. Workflow Ochestration/
│   ├── model_training.py             # Prefect workflow
│   └── README.md
├── 3. Model Deployment/
│   ├── predict_local.py              # Local model serving
│   ├── predict_remote.py             # Remote model serving
│   ├── test.py                       # API testing
│   ├── Dockerfile                    # Container configuration
│   └── README.md
├── 4. Model Monitoring/
│   ├── docker-compose.yml            # Monitoring stack
│   └── README.md
├── datasets/                         # Data directory (empty initially)
├── models/                          # Model storage
├── Test/                            # Testing framework
├── requirements.txt                 # Python dependencies
├── setup.py                        # Package configuration
├── .env                            # Environment variables template
├── GETTING_STARTED.md              # Comprehensive setup guide
└── README.md                       # Main project documentation
```

## What the Script Does

1. **Initializes Git repository** if not already present
2. **Creates comprehensive .gitignore** to exclude:
   - Python cache files and virtual environments
   - Large model files and datasets (to be stored separately)
   - MLflow tracking database and logs
   - IDE and OS specific files
   - Sensitive environment variables

3. **Adds remote repository** pointing to your GitHub repo
4. **Stages all files** for initial commit
5. **Creates detailed commit message** describing the project
6. **Pushes to main branch** on GitHub

## Important Notes

### Before Pushing:
- Ensure you have Git installed and configured with your GitHub credentials
- Make sure you have created the repository on GitHub first
- Consider if you want to make the repository public or private

### After Pushing:
1. **Add Repository Description** on GitHub:
   - "End-to-End Diabetes Prediction MLOps Project with MLflow, Prefect, Flask, and Docker"

2. **Add Topics/Tags**:
   - `mlops`, `machine-learning`, `diabetes-prediction`, `mlflow`, `prefect`, `flask`, `docker`, `python`

3. **Download Datasets**:
   - Follow instructions in `GETTING_STARTED.md` to download datasets from Kaggle
   - Datasets are excluded from Git due to size

4. **Set up GitHub Actions** (Optional):
   - Consider adding CI/CD workflows for automated testing and deployment

## Troubleshooting

### Authentication Issues:
If you encounter authentication errors:
```bash
# Set up Git credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Use GitHub CLI for authentication (recommended)
gh auth login

# Or use Personal Access Token
# Generate token at: https://github.com/settings/tokens
```

### Large File Issues:
If you encounter issues with large files:
- The .gitignore excludes large model files and datasets
- Consider using Git LFS for large files if needed:
```bash
git lfs install
git lfs track "*.pkl"
git lfs track "*.csv"
```

### Repository Already Exists:
If the repository already has content:
```bash
# Pull existing content first
git pull origin main --allow-unrelated-histories
# Then push your changes
git push origin main
```

## Next Steps After Push

1. **Visit your repository**: https://github.com/MuhammadQasim111/DIABETES_ML_OPS
2. **Clone on other machines**:
   ```bash
   git clone https://github.com/MuhammadQasim111/DIABETES_ML_OPS.git
   ```
3. **Follow GETTING_STARTED.md** for complete setup instructions
4. **Download datasets** and start experimenting with the ML pipeline

Your complete Diabetes ML Project is now ready for collaboration and deployment! 🚀
