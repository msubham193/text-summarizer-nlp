import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, jsonify


def summarizer(text):
    print("ll")
    stop_words = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_freq = {}

    return word_freq

    # for word in doc:
    #     if word.text.lower() not in stop_words and word.text.lower() not in punctuation:
    #         if word.text not in word_freq.keys():
    #             word_freq[word.text] = 1
    #         else:
    #             word_freq[word.text] += 1

    # max_freq = max(word_freq.values())
    # for word in word_freq:
    #     word_freq[word] = word_freq[word]/max_freq

    # sent_token = [sent for sent in doc.sents]

    # sent_scores = {}

    # for sent in sent_token:
    #     for word in sent:
    #         if word.text in word_freq.keys():
    #             if sent not in sent_scores.keys():
    #                 sent_scores[sent] = word_freq[word.text]
    #             else:
    #                 sent_scores[sent] += word_freq[word.text]

    # select_len = int(len(sent_token)*0.3)
    # summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    # final_summary = [word.text for word in summary]
    # summary = ' '.join(final_summary)

    return summary


app = Flask(__name__, static_folder='client', static_url_path='/')
CORS(app)


@app.route('/')
@cross_origin()
def home():
    return "Sonu"


@app.route('/summary', methods=['POST'])
@cross_origin()
def summary():
    data = request.get_json()
    return summarizer(data['content'])


if __name__ == '__main__':
    app.run()
