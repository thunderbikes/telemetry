from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.json  # Assuming JSON data is sent from ESP32
    # Process the received data here
    print("Received telemetry data:", data)
    return jsonify({'message': 'Telemetry data received'}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the server
