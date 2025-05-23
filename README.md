# 🚀 End-to-End MLOps Project with Flask

This repository showcases my journey into **Flask** and **MLOps**, documenting each milestone from initial API development to full production-grade ML pipeline deployment.

---

## 🗓️ Project Timeline

| Milestone                                 | Date               |
| ----------------------------------------- | ------------------ |
| Flask & API Development Started           | May 17, 2025       |
| MLflow Integration Initiated              | September 18, 2025 |
| Hyperparameter Optimization with Hyperopt | May 20, 2025       |
| DVC Integration                           | May 21, 2025       |
| ML Pipeline on DagsHub                    | December 23, 2025  |

---

## ✅ Progress Highlights

### 📌 Flask Fundamentals

* Understood WSGI architecture and Flask basics.
* Created dynamic routes using `@app.route`.
* Utilized **Jinja2** for templating and dynamic HTML rendering.

### 📝 Form Handling

* Implemented user forms to capture Name, Email, and Message.
* Managed both `GET` and `POST` methods for form submissions.

### 🔗 Routing & Redirection

* Created variable routes using `<variable>`.
* Applied `redirect()` and `url_for()` for navigation with parameters.

### 📊 Marks Entry System

* Built a form to accept marks for three subjects.
* Calculated average and displayed a result page with `PASS` or `FAIL`.

---

## 🧪 Flask To-Do List API

### ✅ Features

* View, Add, Update, and Delete tasks

### 🔗 Endpoints

| Method | Route              | Description        |
| ------ | ------------------ | ------------------ |
| GET    | `/`                | Welcome message    |
| GET    | `/items`           | Retrieve all tasks |
| POST   | `/items`           | Add a new task     |
| PUT    | `/items/<item_id>` | Update a task      |
| DELETE | `/items/<item_id>` | Delete a task      |

### 📂 Task Format

```json
{
  "id": int,
  "name": str,
  "description": str
}
```

---

## 📈 MLOps with MLflow

### ✅ Initial Setup

* Created virtual environment and structured MLflow project.
* Launched MLflow UI and explored experiment tracking features.

### 🔮 Experiment Tracking

* Logged model parameters, metrics, and artifacts.
* Used the UI to compare experiments effectively.

### 🏡 House Price Prediction Project

* Trained `RandomForestRegressor` with `GridSearchCV` (3-fold CV).
* Logged Mean Squared Error and hyperparameters.
* Registered models via MLflow Tracking URI.

### 📦 Artifact Management

* Verified creation of `mlruns/` and `artifacts/`.
* Ensured reproducibility through versioned logging.

### 📊 ANN + Hyperopt on Wine Quality Dataset

* Implemented ANN model.
* Tuned hyperparameters using `Hyperopt` (`fmin`, `tpe`, `Trials`).
* Logged RMSE and best parameters.

---

## 📦 Data Version Control with DVC

### ✅ Setup Steps

1. Created virtual environment `dvc_venv`.
2. Installed DVC using `pip install dvc`.
3. Created and tracked `data/` directory.
4. Ran `dvc init` and `dvc add data/data.txt`.
5. Used Git to version control `.dvc` files.
6. Updated DVC tracking after modifying `data.txt`.
7. Noticed hashed data stored in `.dvc/cache/`.

---

## 🔧 Tech Stack

* **Python** 🐍
* **Flask** 🌶️
* **HTML/CSS** 🎨
* **Jinja2** 🧩
* **MLflow** 📈
* **DVC** 📦
* **Hyperopt** 🔍

---

## 🧱 ML Pipeline on DagsHub

### ✅ Setup

* Created and cloned repository from DagsHub.
* Added `README.md` and structured project with `data/raw/data.csv`.
* Created virtual environment `ml_pipeline` and added it to `.gitignore`.
* Defined `params.yaml` with config for preprocessing and training.

### 🔹 Preprocessing

* Built `preprocess.py` to read from `input_path` and save to `output_path`.
* Used `os.makedirs()` to ensure directory creation.

### 🔹 Model Training

* Developed `train.py` with MLflow tracking for:

  * Accuracy
  * Confusion Matrix
  * Classification Report
* Used `GridSearchCV` for hyperparameter tuning.

### 🔹 Evaluation

* Added `evaluate.py` to load `model.pkl`, make predictions, and log final accuracy.

### 🔹 DVC Pipeline Automation

* Created `dvc.yaml` to automate preprocessing, training, and evaluation.
* Ran:

```bash
dvc repro
dvc pull -r origin main
dvc push -r origin main
git add .
git commit -m "final commit"
git push origin main
```

---

This repository marks a complete transition from learning Flask basics to building and tracking reproducible, production-ready ML pipelines with MLOps best practices.
