from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.files['file']
    print(data)
    return "Received POST request"

if __name__ == '__main__':
    app.run(port=3000)
