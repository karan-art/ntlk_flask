from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords as sw
from nltk import FreqDist


# initialize the app
app = Flask(__name__)

# download the model(model for sentence and word tokenization)
nltk.download('punkt')
nltk.download('stopwords')

@app.route('/')
def hello():
    return render_template('form.html')


@app.route('/submit', methods = ["POST"])
def form_data():
    data = request.form.get('text')

    # Perform required operations

    sent_count = len(sent_tokenize(data))
    word_count = len(word_tokenize(data))

    eng_sw = sw.words('english')
    data_sw = []
    for word in word_tokenize(data.lower()):
        if word in eng_sw:
                data_sw.append(word)
    

    freq = FreqDist(word_tokenize(data))


    return render_template('form.html', data_out = f"Sentences: {sent_count}, Words: {word_count}, Stopwords: {data_sw}, Frequency: {dict(freq)}")
    # return 'Form Submitted'

if __name__ == '__main__':
    app.run(debug=True)
