from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alerts', methods=['POST'])
def receive_alert():
    try:
        data = request.json
        #print(data)
        if not data:
            return jsonify({"error": "Invalid data"}), 400
        
        
        return jsonify({"message": "Alert received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)