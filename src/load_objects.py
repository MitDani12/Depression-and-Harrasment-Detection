import pickle
OBJECT_PATH = '../'


def load_harassment_tokenizer():

    harassment_tokenizer_file = open('../harassment-tokenizer.pickle', 'rb')
    harassment_tokenizer = pickle.load(harassment_tokenizer_file)
    harassment_tokenizer_file.close()

    return harassment_tokenizer


def load_harassment_model():

    harassment_model_file = open('../harassment-model.pickle', 'rb')
    harassment_model = pickle.load(harassment_model_file)
    harassment_model_file.close()

    return harassment_model


def load_depression_tokenizer():

    depression_tokenizer_file = open(
        '../depression-tokenizer.pickle', 'rb')
    depression_tokenizer = pickle.load(depression_tokenizer_file)
    depression_tokenizer_file.close()

    return depression_tokenizer


def load_depression_model():

    depression_model_file = open('../depression-model.pickle', 'rb')
    depression_model = pickle.load(depression_model_file)
    depression_model_file.close()

    return depression_model
