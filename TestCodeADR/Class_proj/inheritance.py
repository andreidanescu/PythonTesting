class Parent():
    def __init__(self, last_name, eye_colour):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_colour = eye_colour

    def show_info(self):
        print("Last name " + self.last_name)
        print("Eye color " + self.eye_colour)


class Child(Parent):
    def __init__(self,last_name, eye_color,num_toys):
        Parent.__init__(self,last_name,eye_color)
        self.num_toys = num_toys

    def show_info(self):
        print("Last name " + self.last_name)
        print("Eye color " + self.eye_colour)
        print("Number of toys " + self.num_toys)
        

billy_cyrrus = Parent("Cyrrus","blue")
print(billy_cyrrus.last_name) 

miley_cyrrus = Child("Cyrrus", "grey", "20")
print(miley_cyrrus.num_toys)

billy_cyrrus.show_info()

miley_cyrrus.show_info()
