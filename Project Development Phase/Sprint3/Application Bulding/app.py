import requests
from tensorflow.keras.preprocessing import image
from  tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask,request,render_template,redirect,url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session
app = Flask(__name__)
model =load_model("fruits.h5")
model =load_model("vegitable.h5")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/index.html')
def prediction():
    return render_template('/index.html')
@app.route('/predict',methods=['Post'])
def predict():
    if request.method=='Post':
        f=request.files['images']
        basepath = os.path.dirname(__name__)
        file_path = os.path.join(basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)
        img = image.load.img(file_path,target_size=(128,128))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)
        plant=request.form['plant']
        print(plant)
        if (plant=="vegitable"):
           preds = model.predict_classes(x)
           print(preds)
           df=pd.read_excel('precaution-veg.xlsl')
           print(df.iloc[preds[0]]['caution'])
        else:
             preds =model1.predict_classes(x)

             df=pd.read_excel('precaution-fruits.xlsl')
             print(df.iloc[preds[0]]['caution'])
        return(df.iloc[preds[0]]['caution'])
if __name__ == "__main__":
    app.run(debug=False)
