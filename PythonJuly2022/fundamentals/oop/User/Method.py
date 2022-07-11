

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

nic=User("Nic", "nicemail@email.com")
chris_lucky=User("Great", "whoknows@email.com")

nic.greeting()
chris_lucky.greeting() 