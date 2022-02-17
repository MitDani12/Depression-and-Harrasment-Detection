from flask import Flask, render_template, request

from data_prepare import (clean_text,
                          get_depression_sequences,
                          get_harassment_sequences,
                          validate_depression_text,
                          validate_harassment_text
                          )
from predict import get_depression_prediction, get_harassment_prediction
from result import get_result


app = Flask(__name__)


@app.route('/result', methods=['POST'])
def process_result():

    text = request.form['text-check']
    text = str(text)

    depression_validate_result = validate_depression_text(text)
    harassment_validate_result = validate_harassment_text(text)
    result = get_result(depression_validate_result, harassment_validate_result)

    if (result == 'Neither'):
        return render_template('result.html', result=result)

    depression_sequences = get_depression_sequences(text)
    depression_prediction = get_depression_prediction(depression_sequences)

    harassment_sequences = get_harassment_sequences(text)
    harassment_prediction = get_harassment_prediction(harassment_sequences)

    result = get_result(depression_prediction, harassment_prediction)
    return render_template('result.html', result=result)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
