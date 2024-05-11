from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    # Perform health check logic here
    try:
        # Example: Check database connection, external service availability, etc.
        # If everything is healthy, return a success response
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        # If health check fails, return an error response
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def hello_world():
    return 'Hello, World! This is Flask running in Docker on Alpine Linux.'

if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 3001
    app.run(debug=True, host='0.0.0.0', port=3001)

