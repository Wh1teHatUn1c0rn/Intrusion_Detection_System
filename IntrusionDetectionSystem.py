import json
import requests
import socket


class IntrusionDetection:
    def __init__(self, api_url, threshold):
        self.api_url = api_url
        self.threshold = threshold
        self.local_ip = socket.gethostbyname(socket.gethostname())

    def check_traffic(self):
        # Get the current traffic usage
        traffic = get_current_traffic()

        # Check if the traffic exceeds the threshold
        if traffic > self.threshold:
            payload = {"message": f"Traffic threshold exceeded on {self.local_ip}"}
            headers = {'content-type': 'application/json'}
            response = requests.post(f"{self.api_url}/notification", data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                print("Notification sent to the server")
            else:
                print("Failed to send notification")


detection = IntrusionDetection("http://example.com", 1000)
detection.check_traffic()
