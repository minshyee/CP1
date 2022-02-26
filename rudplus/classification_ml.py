import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_anlysis(docx):
    model = SentimentIntensityAnalyzer()

    score = model.polarity_scores(docx)['compound']

    if score < -0.3:
        pred = 'is dangerous😲 Ask for help.'
    elif score < -0.1:
        pred = 'can be dangerous..🥺 if you need help, please come anytime.'
    elif score < 0.1:
        pred = 'is nice😌 if you need help, please come anytime.'
    else:
        pred = ' very good😊! I hope you stay happy!'
    return pred
