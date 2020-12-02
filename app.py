from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np
import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

app = Flask(__name__, template_folder='template')
app.config["TEMPLATES_AUTO_RELOAD"] = True
import os

@app.route("/")
def home():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./index1.html")

@app.route("/cancer")
def cancer():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./cancer.html")

def ValuePredictorCancer(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load('./cancer_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predictCancer', methods = ["POST"])
def predictCancer():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #cancer
        if(len(to_predict_list)==5):
            result = ValuePredictorCancer(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "You are in HIGH RISK. Please consult the doctor immediately"
    else:
        prediction = "You are absolutely in NO RISK ZONE. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))       

# for diab
    
@app.route("/diabetes")
def diabetes():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./diabetes.html")

def ValuePredictorDiabetes(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        loaded_model = joblib.load('./diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predictDiabetes', methods = ["POST"])
def predictDiabetes():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==6):
            result = ValuePredictorDiabetes(to_predict_list,6)
    
    if(int(result)==1):
        prediction = "You are in HIGH RISK. Please consult the doctor immediately"
    else:
        prediction = "You are absolutely in NO RISK ZONE. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))     

# for heart
    
@app.route("/heart")
def heart():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./heart.html")

def ValuePredictorHeart(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('./heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predictHeart', methods = ["POST"])
def predictHeart():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictorHeart(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "You are in HIGH RISK. Please consult the doctor immediately"
    else:
        prediction = "You are absolutely in NO RISK ZONE. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))   
   
# for kidney
    
@app.route("/kidney")
def kidney():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./kidney.html")

def ValuePredictorKidney(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('./kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predictKidney', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        if(len(to_predict_list)==7):
            result = ValuePredictorKidney(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "You are in HIGH RISK. Please consult the doctor immediately"
    else:
        prediction = "You are absolutely in NO RISK ZONE. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))       

# Liver 
    
@app.route("/liver")
def liver():
    cwd = os.getcwd()
    print(cwd)
    return render_template("./liver.html")

def ValuePredictorLiver(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('./liver_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predictLiver', methods = ["POST"])
def predictLiver():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #liver
        if(len(to_predict_list)==7):
            result = ValuePredictorLiver(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "You are in HIGH RISK. Please consult the doctor immediately"
    else:
        prediction = "You are absolutely in NO RISK ZONE. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction)) 
    
if __name__ == "__main__":
    app.run(debug=False)
