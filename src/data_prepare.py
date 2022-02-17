import re
import string
import pandas as pd
from nltk import PorterStemmer
from nltk.corpus import stopwords
from keras.preprocessing.sequence import pad_sequences
from load_objects import load_harassment_tokenizer, load_depression_tokenizer


def clean_text(text):

    # Remove puncuation
    text = text.translate(string.punctuation)

    # Convert words to lower case and split them
    text = text.lower().split()

    # Remove stop words
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w) >= 3]

    # Clean the text
    text = " ".join(text)
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)

    # Stemming
    text = re.sub(r"\s{2,}", " ", text)

    text = text.split()

    # Convert similar words to a common root word
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)

    return text


def validate_depression_text(text):

    text = text.lower()

    if (
        text == 'i am not depressed' or text == 'i was not depressed' or
        text == 'i have not been depressed' or text == 'this is not depressing' or
        text == 'this was not depressing' or text == 'not depressing'
    ):
        return 0
    else:
        return 1


def validate_harassment_text(text):

    text = text.lower()

    if (
        text == 'i am not depressed' or text == 'i was not depressed' or
        text == 'i have not been depressed' or
        text == 'this is not depressing' or text == 'this was not depressing' or
        text == 'not depressing'
    ):
        return 0
    else:
        return 1


def get_harassment_sequences(text):

    MAX_LEN = 200

    text_series = pd.Series([text])
    text_series = text_series.map(lambda x: clean_text(x))

    harassment_tokenizer = load_harassment_tokenizer()
    harassment_tokens = harassment_tokenizer.texts_to_sequences(
        text_series.values)
    harassment_sequences = pad_sequences(harassment_tokens, maxlen=MAX_LEN)

    return harassment_sequences


def get_depression_sequences(text):

    MAX_LEN = 200

    text_series = pd.Series([text])
    text_series = text_series.map(lambda x: clean_text(x))

    depression_tokenizer = load_depression_tokenizer()
    depression_tokens = depression_tokenizer.texts_to_sequences(
        text_series.values)
    depression_sequences = pad_sequences(depression_tokens, maxlen=MAX_LEN)

    return depression_sequences
