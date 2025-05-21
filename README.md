# 🚀 MLOps End-to-End Project with Flask

This repository documents my journey into **Flask** and **MLOps**, starting from scratch and gradually building a production-ready ML system.

## 📅 Project Timeline

* **Flask & API Development Start:** May 17, 2025
* **MLflow Integration Start:** September 18, 2025
* **Hyperparameter Optimization with Hyperopt:** May 20, 2025
* **DVC Integration:** May 21, 2025

---

## ✅ Progress Log

### 📌 Flask Fundamentals

* Understood Flask's internal working with **WSGI**.
* Built routes, handled requests, and used **Jinja2** for rendering HTML.

### 🧩 Jinja2 Templating

* Dynamically injected content into HTML pages.

### 📝 Form Handling

* Built a form to collect **Name**, **Email**, and **Message**.
* Implemented both **GET** and **POST** methods.

### 🔗 Variable Routing

* Used `<variable>` in URLs for dynamic routing.

### ↺ Redirect with Parameters

* Used `redirect()` and `url_for()` for clean user redirection with parameters.

### 📊 Marks Entry System

* Created a form to input marks for 3 subjects.
* Calculated average and redirected users to display `PASS` or `FAIL`.

---

## 🧪 Flask To-Do List API

Implemented a simple **RESTful API** for a To-Do list application.

### ✅ Features

* View, Add, Update, and Delete tasks

### 🔗 API Endpoints

| Method | Route              | Description        |
| ------ | ------------------ | ------------------ |
| GET    | `/`                | Welcome message    |
| GET    | `/items`           | Retrieve all items |
| POST   | `/items`           | Add a new item     |
| PUT    | `/items/<item_id>` | Update an item     |
| DELETE | `/items/<item_id>` | Delete an item     |

Each item contains:

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

* Created a virtual environment and folder for MLflow.
* Installed MLflow and explored the `mlruns` folder.
* Launched the MLflow UI for experiment tracking.

### 🧪 Experiment Tracking

* Logged metrics, parameters, and models from sample experiments.
* Compared runs using the MLflow UI.

### 🏠 House Price Prediction

* Used `RandomForestRegressor`.
* Applied `GridSearchCV` with 3-fold cross-validation.
* Logged MSE and hyperparameters.
* Registered models with appropriate tracking URI.

### 📦 Artifacts Management

* Verified creation of `mlruns/` and `artifacts/` folders.
* Ensured reproducibility using versioned artifacts.

### 📊 ANN Model with Hyperopt

* Trained ANN on Wine Quality dataset.
* Used Hyperopt (`fmin`, `tpe`, `Trials`) for hyperparameter tuning.
* Tracked RMSE and best parameters with MLflow.

---

## 📦 Data Version Control with DVC

### 📅 Started: May 21, 2025

### ✅ Steps Followed

1. Created a folder named `DVC/` and a virtual environment `dvc_venv`.
2. Installed DVC:

   ```bash
   pip install dvc
   ```
3. Created a `data/` folder and added `data.txt`.
4. Initialized DVC inside the project:

   ```bash
   dvc init
   ```
5. Started tracking data:

   ```bash
   dvc add data/data.txt
   ```
6. Noted: DVC-generated files (e.g., `.dvc`) should be tracked by Git, not the actual data file.
7. Tracked changes using:

   ```bash
   git add data/data.txt.dvc data/.gitignore
   ```
8. Observed versioned hash changes after modifying `data.txt` and re-running:

   ```bash
   dvc add data/data.txt
   git add .
   ```
9. Found versioned data inside `.dvc/cache/` folder.

---

## 🔧 Tech Stack

* **Python** 🐍
* **Flask** 🌶️
* **HTML/CSS** 🎨
* **Jinja2** 🧩
* **MLflow** 📈
* **DVC** 📦
* **Hyperopt** 🔍
