from flask import Flask, render_template, Response, request, redirect
from flask_session import Session
import pickle
import warnings
import pandas as pd

warnings.simplefilter('ignore', UserWarning)

categories = ['Business', 'Entertainment', 'Politics', 'Sport', 'Tech']

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)
with open("vectorizer.pkl", 'rb') as file:
    vectorizer = pickle.load(file)

app = Flask(__name__)
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_prediction():
    news = request.form.get("news")
    if not news:
        return render_template("fail.html")
    else:
        y_pred = [news]
        y_pred = vectorizer.transform(y_pred)
        answer = model.best_estimator_.predict(y_pred)[0]
        answer = answer[0].upper() + answer[1:]
        result = pd.DataFrame(model.best_estimator_.predict_proba(y_pred)[0].round(2), categories, columns=["Probability"]).sort_values(by="Probability",ascending=False)
        return render_template("result.html", news=news, answer=answer, prob=result["Probability"], cat=result.index)