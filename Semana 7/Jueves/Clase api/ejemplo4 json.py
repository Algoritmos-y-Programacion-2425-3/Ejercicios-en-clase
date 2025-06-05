import requests
import json

def main():
    url = "http://httpbin.org/get"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        # FORMA 1
        response_json = response.json()
        print(response_json)
        print(response_json.get("headers"))

      
        

main()