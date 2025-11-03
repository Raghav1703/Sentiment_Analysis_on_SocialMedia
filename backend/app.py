from flask import Flask, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

model=joblib.load(r"C:\Users\Raghav\OneDrive\Desktop\Sentiment_Analysis_on_Social_Media\backend\models\sentiment_model.pkl")
vectorizer=joblib.load(r"C:\Users\Raghav\OneDrive\Desktop\Sentiment_Analysis_on_Social_Media\backend\models\tfidf_vectorizer.pkl")

nltk.download('stopwords', quiet=True)
stop_words=set(stopwords.words('english'))
stemmer=PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    filtered = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return " ".join(filtered)

@app.route('/')
def home():
    return jsonify({"message": "Sentiment Analysis API is running"})

@app.route('/predict',methods=['POST'])
def predict():
    try:
        data=request.get_json()
        text=data.get('text','')

        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        cleaned_text=preprocess_text(text)
        transformed_text=vectorizer.transform([cleaned_text])
        prediction=model.predict(transformed_text)[0]

        sentiment="Positive" if prediction=="Positive" else "Negative"

        return jsonify(
            {
                "text": text,
                "cleaned_text": cleaned_text,
                "sentiment": sentiment
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__=="__main__":
    app.run(debug=True)