import requests
import time
import json

# Define the URL and the headers
url = "https://gamba.matav.cz/gamba/2925"
headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "http://127.0.0.1:5501",
    "referer": "http://127.0.0.1:5501/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}

# Initialize the variable 'a'
a = 1

# Infinite loop to send the requests
while True:
    data = {
        "heslo": "basicPassword123",
        "sazka": a
    }
    response = requests.post(url, headers=headers, data=data)
    print(f"Response: {response.text}")

    # Check response and adjust 'a' accordingly
    if response.status_code == 200:
        try:
            response_data = response.json()
            if "vyhra" in response_data:
                vyhra_value = str(response_data["vyhra"])
                if "-" in vyhra_value:
                    a *= 2  
                else:
                    a = 1  
        except json.JSONDecodeError:
            print("Error decoding JSON from response")

