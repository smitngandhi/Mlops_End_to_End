# 🚀 MLOps End-to-End Project with Flask

This repository documents my journey into **Flask** and **MLOps**, starting from scratch and gradually building a production-ready ML system.

## 📅 Started: May 17, 2025

---

## ✅ Progress Log

- 📌 **Explored Flask Fundamentals**  
  Learned how Flask works under the hood using the **WSGI** protocol. Built routes, handled requests, and served multiple HTML pages using `render_template()`.

- 🧩 **Integrated Jinja2 Templating**  
  Used Flask's templating engine **Jinja2** to inject dynamic content into HTML templates.

- 📝 **Built a Sample Form**  
  Created a `form.html` with fields for **Name**, **Email**, and **Message**.  
  Implemented both **GET** and **POST** methods:
  - `GET`: Loads the form.
  - `POST`: Processes form data using `request.form`.

- 🔗 **Learned Variable Routing**  
  Implemented dynamic URL routing using `<variable>` syntax in Flask.  
  Passed variables to functions via URLs for dynamic content handling.

- 🔄 **Redirect with Dynamic Parameters**  
  Used `redirect(url_for(...))` to redirect users and pass computed parameters through dynamic URLs.

- 📊 **Created a Marks Entry System**  
  Developed a `marks.html` page that takes marks for 3 subjects.  
  Calculated the average and passed it through a dynamic route to a `score` function, which returns `PASS` or `FAIL`.

---

## 🔧 Tech Stack

- Python 🐍  
- Flask 🌶️  
- HTML/CSS 🎨  
- Jinja2 🧩  

---

# 📌 Flask To-Do List API

As part of the project, I implemented a basic **To-Do List API** using Flask with CRUD operations.

## ✅ Features

- View all to-do items
- Add a new item
- Update an existing item
- Delete an item

## 🔗 API Endpoints

| Method | Route               | Description              |
|--------|---------------------|--------------------------|
| GET    | `/`                 | Welcome route            |
| GET    | `/items`            | Retrieve all items       |
| POST   | `/items`            | Add a new item           |
| PUT    | `/items/<item_id>`  | Update an item by ID     |
| DELETE | `/items/<item_id>`  | Delete an item by ID     |

Each item has the following structure:

```json
{
  "id": int,
  "name": "string",
  "description": "string"
}
