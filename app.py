from flask import Flask, render_template, request
from preprocessing.cleaner import clean_text
from model.rules import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input-review')
def input_review():
    return render_template('input_review.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    review = request.form['review']
    clean = clean_text(review)
    sentiment, reason = analyze_sentiment(clean)
    return render_template('hasil.html', original=review, clean=clean, sentiment=sentiment, reason=reason)

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

if __name__ == '__main__':
    app.run(debug=True)
