"""
Here is a simple Python code architecture to represent 3 machines, each with an On and Off button controlling the machine and its LED status. This code uses classes and methods for clarity and expandability
"""
class Machine:
    def __init__(self, name):
        self.name = name #its a instance variable to hold name of machine
        self.is_on = False # you are setting initial status of machine to OFF
        self.led_status = "OFF" # you are setting initial status of LED to OFF
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.led_status = True
            print(f"{self.name} is now ON. LED is {self.led_status}.")
        else:
            print(f"{self.name} is already ON.")
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            self.led_status = "OFF"
            print(f"{self.name} is now OFF. LED is {self.led_status}.")
        else:
            print(f"{self.name} is already OFF.")
# Create instances for 3 machines
machine1 =Machine("Machine 1")
machine2 =Machine("Machine 2")
machine3 =Machine("Machine 3")
# Simulate button presses
machine1.turn_on()  # Turn on Machine 1
machine2.turn_on()  # Turn on Machine 2
machine1.turn_off() # Turn off Machine 1
machine3.turn_on()  # Turn on Machine 3
machine2.turn_off() # Turn off Machine 2
machine3.turn_off() # Turn off Machine 3

"""
For example, the "Machine" class is a blueprint; each individual machine you create from that class is an object, and "turn_on" or "turn_off" are functions (methods) that specify what happens when you interact with those machine objects.
"""