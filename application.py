from flask import Flask, render_template, request, redirect, url_for
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Extract form data
        data = CustomData(cement = float(request.form['cement']),
        blast_furnace_slag = float(request.form['blast_furnace_slag']),
        fly_ash = float(request.form['fly_ash']),
        water = float(request.form['water']),
        superplasticizer = float(request.form['superplasticizer']),
        coarse_aggregate = float(request.form['coarse_aggregate']),
        fine_aggregate = float(request.form['fine_aggregate']),
        age = int(request.form['age']))

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)
        return render_template('prediction.html', results=results)
    
    return render_template('form.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        return redirect(url_for('form'))
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)