from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('sonar_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index-1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_data = request.form['sonar_data']
        values = [float(x.strip()) for x in raw_data.split(',') if x.strip() != '']

        if len(values) != 60:
            return jsonify({'result': f'Error: 60 values chahiye, mila {len(values)}'})

        input_arr = np.array(values).reshape(1, -1)
        prediction = model.predict(input_arr)[0]
        result = "Mine 💣" if prediction == 'M' else "Rock 🪨"
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)