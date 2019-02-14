from pprint import pprint as pp

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/mpesaHook', methods=['POST'])
def mpesa_hook():
    print('\n\n--- Received M-Pesa webhook ---\n\n')
    content = request.json
    pp(content)
    print('\n\n--- End ---\n\n')
    return jsonify({"statusCode": 200, "status": "success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
