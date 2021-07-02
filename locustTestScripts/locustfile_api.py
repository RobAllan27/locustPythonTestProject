from __future__ import print_function
from locust import HttpUser, task, between, events
from json import JSONDecodeError

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new API test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("The API test is ending")

headersToSend ={
"Host": "my.name.com",
"User-Agent":"locust",
}

class WebsiteTestUserFirst(HttpUser):
    wait_time = between(1,1)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # print('Starting the test here - first user')
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # print('Stopping the test here -  first user')
        pass

    @task(1)
    def call_Post_Player(self):
        with self.client.post("http://localhost:5010/player", headers=headersToSend, json={"name": "Dave Harro", "position": "Attacker"}, catch_response=True) as response:
            try:
                if response.json()["success"] != True:
                    response.failure("Did not get expected value in success")
                if response.json()["regoNumber"] != 12345:
                    response.failure("Did not get expected value in regoNumber") 
                if response.status_code != 201:
                    response.failure("Did not get expected response status code") 
                if response.elapsed.total_seconds() > 5.00:
                    response.failure("Request took too long")       
            except JSONDecodeError:
                    response.failure("Response could not be decoded as JSON")
            except KeyError:
                    response.failure("Response did not contain expected key 'success' or 'regoNumber'")

    @task(1)
    def call_Delete_Player(self):
        with self.client.delete("http://localhost:5010/player", headers=headersToSend, json={"name": "Dave Harro", "position": "Attacker"}, catch_response=True) as response:
            try:
                if response.json()["success"] != True:
                    response.failure("Did not get expected value in success")
                if response.json()["regoNumber"] != 22:
                    response.failure("Did not get expected value in regoNumber") 
                if response.status_code != 200:
                    response.failure("Did not get expected response status code") 
                if response.elapsed.total_seconds() > 5.00:
                    response.failure("Request took too long")       
            except JSONDecodeError:
                    response.failure("Response could not be decoded as JSON")
            except KeyError:
                    response.failure("Response did not contain expected key 'success' or 'regoNumber'")
    @task(1)
    def call_Get_Players(self):
        with self.client.get("http://localhost:5010/players", headers=headersToSend, catch_response=True) as response:
            try:
                if response.status_code != 200:
                    response.failure("Did not get expected response status code") 
                if response.elapsed.total_seconds() > 5.00:
                    response.failure("Request took too long")       
            except JSONDecodeError:
                    response.failure("Response could not be decoded as JSON")            
