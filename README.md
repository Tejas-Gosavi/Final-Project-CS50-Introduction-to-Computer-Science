# News classification  web app
Hello, My name is **Tejas Gosavi**.

This is my **CS50: Introduction to Computer Science** final project.

This is a NLP(Natural language processing) based web app which classifies news.

We give news title/description as input and as a output it classifies news in certain category.

Dataset used for this project is bbc news headlines dataset which i downloaded from **kaggle**.

Algorithm used to predict category is **Multinomial Naive Bayes**, which is
very much famous/used for text classification. It is based on **Bayes Theorem**.

**🌟 Project video - https://youtu.be/2BAPLb8DwJ0 ✌️**

### Prerequisites
You must have any of thses Tool installed
  - Jupyter notebook
  - Visual studio code

### Project Structure
1. model.ipynb - This contains code of our Machine Learning model to predict news category based on training data in ***bbc-text.csv*** file. It saves model algorithm and vectorizer in .pkl file.

2. app.py / application.py - This contains Flask API that take News title/description through GUI call, classifies in the predicted category based on
model algorithm.

3. templates - This folder contains dynamic web templates.

4. static - This folder contains static files like stylesheets, images, etc.

5. requirements.txt - This file contains python packages required to run the project.

### Running the project
1. Ensure that you are in the project home directory and run below command in cmd to start given Flask web app
```
flask run
```
By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000

3. and... Voila our web app is started and now enter news title or descritption to classify in its category.
