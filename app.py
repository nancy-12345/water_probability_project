#Libraries
import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    ph = request.form['ph']
    hardness = request.form['hardness']
    solids = request.form['solids']
    chloramines = request.form['chloramines']
    conductivity = request.form['conductivity']
    organic_carbon = request.form['organic carbon']
    trihalomethanes = request.form['trihalomethanes']
    turbidity = request.form['turbidity']

    prediction = loadedModel.predict([[ph, hardness, solids, chloramines, conductivity, organic_carbon, trihalomethanes, turbidity]])[0]

    if prediction == 0:
        prediction = "Not Potable"
    else:
        prediction = "Potable"

    return render_template('index.html', output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)