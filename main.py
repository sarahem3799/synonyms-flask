from flask import Flask, render_template, request
from nltk.corpus import wordnet
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('form.html')


@app.route("/", methods=["post"])
def syn():
    inp = request.form['in']
    synonym = []
    for syn in wordnet.synsets(inp):
        for lm in syn.lemmas():
            synonym.append(lm.name())
    return render_template('form.html', syn=synonym)


if __name__ == '__main__':
    app.run(debug=True)
