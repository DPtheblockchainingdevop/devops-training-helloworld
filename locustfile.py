import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5.0, 9.0)
    
    @task
    def index(l):
        l.client.get("/")