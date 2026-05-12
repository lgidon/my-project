import os
from flask import Flask
import time


# Initialize the Flask application
app = Flask(__name__)

MSG_CONTENT = os.environ.get('APP_GREETING', 'Hello, World!')

APP_PASSWORD = os.environ.get('APP_PASSWORD')

READINESS_FAIL = os.environ.get('SIMULATE_READINESS_FAIL') == 'true'

LIVENESS_HANG = os.environ.get('SIMULATE_LIVENESS_HANG') == 'true'

# Define a route for the root URL
@app.route('/')
def hello_world():
	if APP_PASSWORD != 'topsecret':
		return "Access Denied: Invalid Password", 401
	return f"Success! {MSG_CONTENT}"

@app.route('/health')
def health_check():
	if LIVENESS_HANG:
		time.sleep(30)
	if READINESS_FAIL:
		return "Error", 500
	else:
		return "OK", 200

# Run the app if this file is executed
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
