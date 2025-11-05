import requests
import json
import random
import config
import time


class DataProvider:

    def __init__(self):
       self.service_b_url = config.SERVICE_B_HTTP_API_ENDPOINT
       self.config_file_path = config.PAYLOADS_FILE_PATH
       self.active_time_period = config.ACTIVE_TIME_PERIOD
       self.between_time_period = config.BETWEEN_TIME_PERIOD


    def load_config(self):
       with open(self.config_file_path, 'r') as f:
          return json.load(f)

    def get_random_item(self, data : list):
        if not data:
            raise Exception(f"no data in JSON config file, or config file is not valid")
        random_item = random.choice(data)
        return random_item

    def call_service_b(self, data: json):
        url = f"{self.service_b_url}"
        response = requests.post(
            url,
            json=data,
            headers= {"content-type" : "application/json"},
            verify=False #For local HTTPS
            )

        if not response.ok:
            raise Exception(f"Failed to send data", detail=response.text)
        return response.json()
    
    def run(self):
        data_array = self.load_config()
        start_time = time.time()
        request_count = 0
        print(f" Starting Service A - will run for {self.active_time_period} seconds")
        while (time.time() - start_time < self.active_time_period):
            random_item = self.get_random_item(data=data_array)
            success = self.call_service_b(data=random_item)
            request_count += 1

            # wait before next request
            if(time.time() - start_time) < self.active_time_period:
                time.sleep(self.between_time_period)
        elapsed_time = time.time() - start_time
        print(f"\n Completed: {request_count} requests sent in {elapsed_time:.2f} seconds")

            
    
if __name__ == "__main__":
    provider = DataProvider()
    provider.run()
    

     





