from flask import Flask, request, jsonify   
from business import get_data
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Welcome to CICD pipeline -##Jenkins'

@app.route('/api', methods=['GET'])
def api():
    data = get_data()
    data = {
        'data': data
    }

    
    return jsonify(data)
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
