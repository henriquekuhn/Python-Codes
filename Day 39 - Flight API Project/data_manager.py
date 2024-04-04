from dotenv import load_dotenv
import os
import requests

load_dotenv()

#### SHEETY AUTHENTICATION ####

username = "766c71604fb86ad8fb12cc376c3205e4"
projectName = "flightDeals"
sheetName = "prices"
sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}"
    }

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=sheety_endpoint, headers=bearer_headers)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data
    

    def update_destination_data(self):
        #print(self.destination_data)
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            #print(response.text)
    


