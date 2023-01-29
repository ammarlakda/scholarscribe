from flask import Flask, request, redirect, url_for
import os
from summarize import *
from speech_text import *
from addToNotion import createPage

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

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
    # saves the file
    if file and allowed_file(file.filename):
        # be careful with this
        filename = file.filename
        file.save('backend', filename)
        # I think this downloads the file, but I can be wrong
        return redirect(url_for('download_file', name=filename))
    #turn data into string
    transcript = speech_text(filename)

    #summarize the transcript
    summarize = split_article(transcript)
    # add page to notion
    createPage(filename, summarize)
    return




if __name__ == '__main__':
    app.run(port=3000)
