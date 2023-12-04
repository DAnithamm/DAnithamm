from locust import task, constant, User


class MyTest(User):
    wait_time=constant(1)

    @task
    def say_hello(self):
        print("hello world")
    @task
    def wear_mask(self):
        print("wear Mask! Stay safe.")
    @task
    def say_goodbye(self):
        print("Good bye")

