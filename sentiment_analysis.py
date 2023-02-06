from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

def get_sentiment(text):
    # Get sentiment scores
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

while True:
    text = input("Enter a sentence or paragraph: ")
    sentiment_scores = get_sentiment(text)
    print(sentiment_scores)
