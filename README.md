# Professor Summary – MLOps Lab Automation Pipeline
This repository contains my work for the MLOps automation lab. The main goal of this project is to show how a machine learning model can be trained, evaluated, versioned, and stored automatically using GitHub Actions. The workflow creates a complete CI/CD process that runs on every push and saves all results inside the repository.

## What This Project Does
- Trains a machine learning model using synthetic data created during each run
- Uses a RandomForestClassifier as my own change from the base lab
- Saves each trained model with a timestamp for version tracking
- Evaluates the model and stores the F1 Score inside the metrics folder
- Stores data files, model files, and metrics inside the repository
- Automatically commits new models and metrics back to GitHub
- Includes unit tests that check training, evaluation, and file creation

## GitHub Actions Automation
The workflow file train_eval_pipeline.yml installs the required Python packages, generates a timestamp, trains the model, evaluates it, saves the output files, and pushes them back to the repository. It runs whenever I push to the main branch or when I trigger it manually from the Actions tab.

## How to Use This Repository
Clone the repository  
git clone https://github.com/Lochan9/MLOps-lab5.git  
cd MLOps-lab5

Install the required Python packages  
pip install -r requirements.txt

Run model training  
python src/train_model.py --timestamp 12345

Run model evaluation  
python src/evaluate_model.py --timestamp 12345

Run unit tests  
pytest

Trigger the GitHub Actions workflow  
git add .  
git commit -m "run pipeline"  
git push

After pushing, the workflow will train a model, evaluate it, save the files, and commit the results back to the repository automatically.


