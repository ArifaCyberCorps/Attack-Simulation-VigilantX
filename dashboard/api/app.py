from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status": "running", "pipeline": "active", "alerts_processed": 42})

if __name__ == '__main__':
    # Dashboard API for prototype demo
    app.run(port=5000, debug=True)