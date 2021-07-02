from __future__ import print_function
from locust import HttpUser, task, between, events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")


class WebsiteTestUserFirst(HttpUser):
    wait_time = between(0, 0.001)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # print('Starting the test here - first user')
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # print('Stopping the test here -  first user')
        pass

    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:5000")

class WebsiteTestUserSecond(HttpUser):
    wait_time = between(0, 0.001)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # print('Starting the test here - second user')
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        # print('Stopping the test here - second user')
        pass

    @task(1)
    def hello_world_again(self):
        self.client.get("http://localhost:5000/helloagain/")