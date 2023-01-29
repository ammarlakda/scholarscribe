from flask import Flask, request, redirect, url_for, make_response
import os
from summarize import *
from classification import *
from speech_text import *
from addToNotion import createPage
from flask_cors import CORS

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def helloworld():
    return 'helloworld'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def handle_post_request():
    #receives video/audio file from front-end
    file = request.files['file']
    print("file received")
    filename = ""
    print(file.filename)
    # saves the file
    if file:
        # be careful with this
        filename = file.filename
        file.save(filename)

    #turn data into string
    print('getting transcript')
    transcript = speech_text(filename)

    #summarize the transcript
    print('summarizing')
    summarize = split_article(transcript)
    # calling classify
    grouped = classifySummary(summarize)
    # add page to notion
    createPage(filename, grouped)
    response = make_response({"summary": grouped})
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
