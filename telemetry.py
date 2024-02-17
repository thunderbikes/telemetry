import urequests as requests  # MicroPython's requests library

telemetry_data = {'temperature': 25.5, 'humidity': 50.0}  # Example telemetry data

url = 'http://localhost:5000/telemetry'  # Replace with your computer's IP address
response = requests.post(url, json=telemetry_data)

print(response.text)
