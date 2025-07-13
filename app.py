from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "model.joblib"
DATA_PATH = "car.csv"

# Train the model once and save


def train_model():
    data = pd.read_csv(DATA_PATH)
    x = data.iloc[:, [0, 1, 2, 3]].values
    y = data.iloc[:, -1].values
    model = DecisionTreeRegressor()
    model.fit(x, y)
    joblib.dump(model, MODEL_PATH)


# Ensure model is trained before running
if not os.path.exists(MODEL_PATH):
    train_model()

model = joblib.load(MODEL_PATH)


@app.route('/')
def carpage():
    return render_template("car.html", data1=None, data2=None)


@app.route('/Car', methods=["POST"])
def car():
    try:
        Fueltype = int(request.form.get("fueltype"))
        Enginetype = int(request.form.get("enginetype"))
        Enginesize = float(request.form.get("enginesize"))
        Horsepower = float(request.form.get("horsepower"))

        predict_price = model.predict(
            [[Fueltype, Enginetype, Enginesize, Horsepower]])

        return render_template(
            "car.html",
            data1=round(predict_price[0], 2),
            data2=round(predict_price[0] * 82.04, 2)
        )
    except Exception as e:
        return f"An error occurred: {e}", 400


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
