from load_objects import load_depression_model, load_harassment_model

def get_depression_prediction(X):

    depression_model = load_depression_model()
    depression_prediction = depression_model.predict_classes(X)
    return depression_prediction[0][0]

def get_harassment_prediction(X):

    harassment_model = load_harassment_model()
    harassment_prediction = harassment_model.predict_classes(X)
    return harassment_prediction[0][0]
