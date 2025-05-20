# 🚀 MLOps End-to-End Project with Flask

This repository documents my journey into **Flask** and **MLOps**, starting from scratch and gradually building a production-ready ML system.

## 📅 Started: May 17, 2025

---

## ✅ Progress Log  

### 📌 Explored Flask Fundamentals

* Learned how Flask works under the hood using the **WSGI** protocol.
* Built routes, handled requests, and served multiple HTML pages using `render_template()`.

### 🧩 Integrated Jinja2 Templating

* Utilized Flask's templating engine **Jinja2** to inject dynamic content into HTML templates.

### 📝 Built a Sample Form

* Created `form.html` with fields for **Name**, **Email**, and **Message**.
* Implemented both **GET** and **POST** methods:

  * `GET`: Loads the form.
  * `POST`: Processes submitted form data using `request.form`.

### 🔗 Learned Variable Routing

* Used dynamic URL routing with `<variable>` syntax in Flask.
* Passed variables to route functions via URLs for dynamic content handling.

### 🔄 Redirect with Dynamic Parameters

* Implemented `redirect(url_for(...))` to redirect users and pass computed parameters through dynamic URLs.

### 📊 Created a Marks Entry System

* Developed a `marks.html` page to accept marks for 3 subjects.
* Calculated the average and passed it through a dynamic route to a `score` function.
* Displayed result as `PASS` or `FAIL` based on the average.

---

## 🔧 Tech Stack

* Python 🐍
* Flask 🌶️
* HTML/CSS 🎨
* Jinja2 🧩

---

# 📌 Flask To-Do List API

As part of the project, I implemented a basic **To-Do List API** using Flask with full CRUD operations.

## ✅ Features

* View all to-do items
* Add a new item
* Update an existing item
* Delete an item

## 🔗 API Endpoints

| Method | Route              | Description          |
| ------ | ------------------ | -------------------- |
| GET    | `/`                | Welcome route        |
| GET    | `/items`           | Retrieve all items   |
| POST   | `/items`           | Add a new item       |
| PUT    | `/items/<item_id>` | Update an item by ID |
| DELETE | `/items/<item_id>` | Delete an item by ID |

Each item has the following structure:

```json
{
  "id": int,
  "name": "string",
  "description": "string"
}
```

---

# 📈 MLOps with MLflow

## 📅 Started: September 18, 2025

### ✅ Initial Setup

* Created a folder named `mlflow`.
* Set up a virtual environment inside the folder.
* Created `requirements.txt` with necessary dependencies.
* Installed MLflow using `pip install mlflow`.

### 🧪 Experiment Tracking

* Created `get-started.ipynb` to test MLflow tracking.
* Ran MLflow UI using the command:

```bash
mlflow ui
```

* Observed the MLflow dashboard and explored the `mlruns` folder.
* `mlruns` automatically tracks experiments with metrics, parameters, models, and artifacts.

---

## 🏠 House Price Prediction with MLflow

### 📅 Started: September 19, 2025

* Built a full regression model to predict house prices.
* Performed **hyperparameter tuning** using `GridSearchCV` with `RandomForestRegressor`.
* Used `cv=3` to perform 3-fold cross-validation.
* Logged every hyperparameter using:

```python
mlflow.log_params(params)
```

* Logged evaluation metric (MSE) using:

```python
mlflow.log_metric("mse", mse)
```

### 🔁 Model Versioning and Tracking

* Set tracking URI:

```python
mlflow.set_tracking_uri("http://127.0.0.1:5000")
```

* Parsed the tracking scheme using:

```python
from urllib.parse import urlparse
urlparse(mlflow.get_tracking_uri()).scheme
```

* Based on the URI type:

  * If **not a file** (e.g., remote server), registered the model using:

```python
mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="Best Random Forest Model")
```

* Else, logged the model without registration:

```python
mlflow.sklearn.log_model(model, artifact_path="model", signature=signature, input_example=X_test[:5])
```

### 📦 Artifacts Logged

After the run:

* `mlruns/` created automatically
* Inside it:

  * `artifacts/`: Stores model metadata (MLmodel file, Conda env, etc.)
  * `metrics/`: Logged evaluation metrics
  * `params/`: Logged model parameters

Artifacts make the experiment reproducible and the model deployable.


