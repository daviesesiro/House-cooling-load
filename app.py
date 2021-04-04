from flask import Flask, request, render_template, redirect
from model import make_log_prediction

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'] )
def predict():
    data = request.json
    return make_log_prediction(data['surfaceArea'], data['overallHeight'], data['heatingLoad'])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)