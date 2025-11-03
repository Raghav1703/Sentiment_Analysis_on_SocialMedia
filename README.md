#  Sentiment Analysis on Social Media
A full-stack project that performs sentiment analysis on social media text posts (like tweets) to classify them as Positive or Negative using Natural Language Processing (NLP).
The project includes a trained machine learning model integrated with a Flask backend and a modern React frontend.

## Features
- Analyze sentiment of user-entered text in real-time
- Preprocessing pipeline for tweet cleaning
- Machine Learning model (TF-IDF + Logistic Regression)
- Flask REST API backend
- Interactive React frontend for real-time prediction display
- Modular project structure for scalability

## Project Structure
<pre> sentiment-analysis/ │ ├── backend/ │ ├── app.py # Flask API serving model predictions │ ├── requirements.txt # Python dependencies for backend │ ├── frontend/ │ ├── src/ │ │ ├── App.js # React entry point for UI │ │ ├── components/ # React components for UI sections │ │ ├── assets/ # Optional images/icons │ ├── package.json # Frontend dependencies │ ├── notebooks/ │ ├── sentiment_model.ipynb # Model training & preprocessing notebook │ └── README.md # Project documentation </pre>


## Tech Stack
Backend:
- Python, Flask, Flask-CORS
- scikit-learn, pandas, nltk

Frontend:
- React (JavaScript), Axios, HTML, CSS

Model:
- TF-IDF Vectorizer
- Logistic Regression Classifier

