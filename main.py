from flask import Flask, request, jsonify
from logic import process

app = Flask(__name__)

@app.route('/discovery', methods=['POST', 'GET'])
def request_process():
    req_lat = float(request.args.get('lat'))
    req_lon = float(request.args.get('lon'))

    data = process(req_lat, req_lon)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port='50000')