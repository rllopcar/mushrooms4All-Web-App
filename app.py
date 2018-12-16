from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pandas as pd
import numpy as np
from resources.modelling import data_enconding
from sklearn.externals import joblib
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dataset')
def about():
    return render_template('dataset.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        capshape = request.form['capshape']
        capsurface = request.form['capsurface']
        capcolor = request.form['capcolor']
        bruises = request.form['bruises']
        odor = request.form['odor']
        gillattachment = request.form['gillattachment']
        gillspacing = request.form['gillspacing']
        gillsize = request.form['gillsize']
        gillcolor = request.form['gillcolor']
        stalkshape = request.form['stalkshape']
        stalkroot = request.form['stalkroot']
        #if stalkroot=='?':
        #        n = ['b','c','u','e','z','r']
        #        stalkroot = random.choice(n)
        stalksurfaceabovethering = request.form['stalksurfaceabovethering']
        stalksurfacebelowthering = request.form['stalksurfacebelowthering']
        stalkcolorabovethering = request.form['stalkcolorabovethering']
        stalkcolorbelowthering = request.form['stalkcolorbelowthering']
        veiltype = request.form['veiltype']
        veilcolor = request.form['veilcolor']
        ringnumber = request.form['ringnumber']
        ringtype = request.form['ringtype']
        sporeprintcolor = request.form['sporeprintcolor']
        population = request.form['population']
        habitat = request.form['habitat']

        data = pd.DataFrame([[capshape], [capsurface], [capcolor], [bruises], [odor], [gillattachment], [gillspacing], [gillsize], [gillcolor], [stalkshape], [stalkroot], [stalksurfaceabovethering], [stalksurfacebelowthering], 
                [stalkcolorabovethering], [stalkcolorbelowthering], [veiltype], [veilcolor], [ringnumber], [ringtype], [sporeprintcolor], [population], [habitat]]).T
        data.columns = ["cap.shape", "cap.surface","cap.color","bruises","odor","gill.attachment",
                                            "gill.spacing","gill.size","gill.color","stalk.shape","stalk.root",
                                            "stalk.surface.above.ring","stalk.surface.below.ring","stalk.color.above.ring",
                                            "stalk.color.below.ring","veil.type","veil.color","ring.number","ring.type","spore.print.color",
                                            "population","habitat"]
        
        mushroom_encoded = np.array([data_enconding(data)])        
        print('#########', mushroom_encoded.shape)
        clf = joblib.load('resources/randomForest.pkl')
        prediction = clf.predict(mushroom_encoded)
        print('###########', prediction)

        return render_template('result.html', prediction = prediction)


if  __name__ == '__main__':
    app.secret_key='secret123'
    app.run()

