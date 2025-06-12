from flask import Flask, render_template, request
from preprocessing.cleaner import clean_text
from model.rules import analyze_sentiment
from preprocessing.stemmer import stem_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input-review')
def input_review():
    return render_template('input_review.html')

@app.route('/process', methods=['POST'])
def process():
    review = request.form['review_text']
    clean = clean_text(review)
    stemmed = stem_text(clean)
    sentiment, reason, confidence = analyze_sentiment(stemmed)
    return render_template('hasil.html', original=review, clean=clean, stemmed=stemmed,
                           sentiment=sentiment, reason=reason, confidence=confidence)

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

if __name__ == '__main__':
    app.run(debug=True)
