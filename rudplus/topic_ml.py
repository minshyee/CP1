import pickle
# from keybert import KeyBERT
import os

def extract_keywords(doc):

    FILENAME = 'model_keyBERT.pkl'
    MODEL_PATH = os.path.abspath(os.path.join(os.getcwd(), FILENAME))
    print(MODEL_PATH)

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(open('model_keyBERT.pkl', 'rb'))

    keywords = model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words='english', use_maxsum=True, nr_candidates=20, top_n=5)
    return keywords[0][0], keywords[1][0], keywords[2][0], keywords[3][0], keywords[4][0]

