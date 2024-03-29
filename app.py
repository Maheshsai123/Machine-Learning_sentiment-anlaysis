from flask import Flask, render_template, request
from textblob import TextBlob
import emojis
import pandas as pd

app = Flask(__name__)

# Load dataset containing reviews
reviews_df = pd.read_csv('final_df.csv')

def analyze_sentiment(review_text):
    """Analyze sentiment of review text."""
    analysis = TextBlob(review_text)
    sentiment = analysis.sentiment.polarity
    return sentiment

def generate_emoji(sentiment):
    """Generate emoji based on sentiment polarity."""
    if sentiment > 0:
        return emojis.encode(":grinning:")  # Positive emoji
    elif sentiment < 0:
        return emojis.encode(":disappointed:")  # Negative emoji
    else:
        return emojis.encode(":neutral_face:")  # Neutral emoji

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render home page and handle form submission."""
    if request.method == 'POST':
        review_text = request.form['review_text']
        if review_text:
            sentiment = analyze_sentiment(review_text)
            emoji = generate_emoji(sentiment)
            return render_template('result.html', review_text=review_text, sentiment=sentiment, emoji=emoji)
        else:
            return render_template('index.html', error="Please enter a review.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0",)

