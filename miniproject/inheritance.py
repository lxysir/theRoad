class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

molly_hock = Child("Hock", "yellow", 5)
print(molly_hock.last_name, molly_hock.number_of_toys)
