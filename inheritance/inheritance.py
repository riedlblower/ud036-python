class Parent():                               # Class
    def __init__(self, last_name, eye_color): # Constructor
        print ("Parent Constructor Called")
        self.last_name = last_name            # Instance variable
        self.eye_color = eye_color            # Instance variable

    def show_info(self):                      # Instance methood
        print "Last Name - " + self.last_name
        print "Eye Color - " + self.eye_color

class Child(Parent):      # inheritance
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):    # method overriding
        print "Last Name - " + self.last_name
        print "Eye Color - " + self.eye_color
        print "Number of toys - " + str(self.number_of_toys)


print "\n" * 5    # print blank lines to somewhat clear the page

billy_cyrus = Parent("Cyrus", "blue")         # Instance
#billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
#print (miley_cyrus.last_name)
#print (miley_cyrus.number_of_toys)
