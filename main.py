import joblib
from flask import Flask, request, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)
model = joblib.load('models/forest_reg.pkl')
scaler = joblib.load('transformers/scaler.joblib')
encoder = joblib.load('transformers/encoder.joblib')


@app.route('/')
def home():
    return render_template('index.html', prediction="$0.00")


@app.route('/predict', methods=['POST'])
def predict():
    data = []
    for index, field in enumerate(request.form.values()):
        if index == 0 or index == 2:
            data.append(int(field))
        elif index == 1:
            data.append(float(field))
        elif index > 2:
            data.append(field)

    df = pd.DataFrame({
        'age': data[0],
        'bmi': data[1],
        'children': data[2],
        'sex': data[3],
        'region': data[4],
        'smoker': data[5],
    }, index=[0])

    # scale numerical data
    scaled_data = scaler.transform(df[['age', 'bmi', 'children']])
    # encode categorical data
    encoded_data = encoder.transform(df[['sex', 'region', 'smoker']]).toarray()
    X = np.hstack([scaled_data, encoded_data])
    prediction = round(float(model.predict(X)), 2)

    return render_template("index.html", prediction=f"${prediction}")


if __name__ == '__main__':
    app.run(debug=True)
