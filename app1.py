import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_features = [float(x) for x in request.form.values()]
        input_array = np.array(raw_features).reshape(1, -1)

        prediction = model.predict(input_array)

        output = str(prediction[0])    

    # Return the prediction
        return render_template("index.html", prediction_text=f"Predicted Ethnicity: {output}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error processing request: {str(e)}"
                           )

if __name__ == "__main__":
    app.run(debug=True)
