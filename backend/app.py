from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return 'helloworld'


@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.files['file']
    if data:
        print('true')

if __name__ == '__main__':
    app.run(port=3000)
