
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, jsonify
from text_summarizer import summarizer

# summarizer = load(open('summarizer.joblib', 'rb'))


app = Flask(__name__, static_folder='client', static_url_path='/')
CORS(app)


@app.route('/')
@cross_origin()
def home():
    return "Sonu"


@app.route('/summary', methods=['GET','POST'])
@cross_origin()
def summary():
    if request.method == 'POST':
       data = request.get_json()
       
    return summarizer(data['content'])


if __name__ == '__main__':
    app.run()
