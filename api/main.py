from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy in-memory data
data = {
    "message": "Hello, world!",
    "count": 0
}

# GET endpoint
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(data)

     # POST endpoint
@app.route('/update', methods=['POST'])
def update_message():
    json_data = request.get_json()
    message = json_data.get('message')
    if message:
        data['message'] = message
        data['count'] += 1
        return jsonify({"status": "updated"}), 200

if __name__ == '__main__':
    app.run(debug=True)
