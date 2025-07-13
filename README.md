# 🚗 Car Price Prediction using Flask and Decision Tree Regressor

This project is a simple machine learning-powered web application to predict car prices based on user inputs such as fuel type, engine type, engine size, and horsepower. The application is built with **Flask**, uses **scikit-learn's DecisionTreeRegressor**, and provides both USD and INR price predictions.

---

## 🔧 Technologies Used

* **Python 3**
* **Flask (Web Framework)**
* **Pandas (Data Handling)**
* **Scikit-learn (ML Model)**
* **Joblib (Model Persistence)**
* **Bootstrap 5 (Frontend Styling)**

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── app.py                # Main Flask Application
├── car.csv                # Training Data (Features & Target)
├── model.joblib           # Saved Machine Learning Model
├── requirements.txt       # Project Dependencies
├── templates/
│   └── car.html           # HTML Template for Frontend
└── static/                # (Optional) For static files like CSS, JS, images
```

---

## 🚀 Features

✅ Predicts **Car Price (USD)** and **Car Price (INR)**
✅ User-friendly **Bootstrap-based Interface**
✅ Persistent trained model using **Joblib** (no retraining on every request)
✅ **Production-ready** Flask app structure

---

## 📊 Dataset (car.csv)

The `car.csv` contains synthetic or real-world data with the following columns:

| Fuel Type | Engine Type | Engine Size | Horsepower | Price (USD) |
| --------- | ----------- | ----------- | ---------- | ----------- |
| 0 / 1     | 0 / 1       | float       | float      | float       |

* `Fuel Type`: 0 = Petrol, 1 = Diesel
* `Engine Type`: 0 = Manual, 1 = Automatic

---

## 🔥 Running Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/lovnishverma/Car-Price-Prediction.git
cd Car-Price-Prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## 🏭 Running in Production

For production deployments, use **Gunicorn**:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Or deploy on **Render / Railway / Huggingface** using this `requirements.txt`.

---

## 💡 Example Usage

| Input Field | Sample Value |
| ----------- | ------------ |
| Fuel Type   | 0            |
| Engine Type | 1            |
| Engine Size | 1.6          |
| Horsepower  | 120          |

**Output:**
Predicted Price (USD): **\$18,000**
Predicted Price (INR): **₹1,47,6720**

---

## 🌐 Live Demo

> [View on Render](https://car-price-prediction-2dgn.onrender.com/)

---

## 📥 Requirements

```
Flask==3.0.3
pandas==2.2.2
scikit-learn==1.5.0
joblib==1.4.2
```

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## ✨ Author

**Lovnish Verma**
[Portfolio Website](https://lovnishverma.github.io/)
[GitHub](https://github.com/lovnishverma)

---
