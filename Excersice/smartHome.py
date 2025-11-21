class smartHome:

    def __init__(self, device):
        self.device_name = device
        self.is_on = False
        self.led = False
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.led = True
            print("Turning on " + self.device_name)
            if self.device_name == "light":
                print("it brightens the room")
            elif self.device_name == "heater":
                print("it heats the room")
            elif self.device_name == "fan":
                print("it cools the room")
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            self.led = False
            print("Turning off " + self.device_name)
            if self.device_name == "light":
                print("it darkens the room")
            elif self.device_name == "heater":
                print("it stops heating the room")
            elif self.device_name == "fan":
                print("it stops cooling the room")

light = smartHome("light")
heater = smartHome("heater")
fan = smartHome("fan")

light.turn_on()
heater.turn_on()
fan.turn_on()
light.turn_off()
heater.turn_off()
fan.turn_off()

"""
Here’s a story for you to write the code from:

Imagine a smart home with three devices: a light bulb, a fan, and a heater. Each device can be turned on or off by pressing a button. When the device is on, a small light (LED) next to it glows to show it’s active. When it’s off, the LED goes dark.

The light bulb brightens the room when switched on. The fan cools the air, and the heater warms up the space. Each device remembers whether it is currently on or off, and its LED reflects the status instantly.

One day, the homeowner wants to control these devices individually. If the light bulb is off and the button is pressed, the light turns on and the LED lights up. Pressing the button again turns it off and the LED goes off. The same happens independently with the fan and the heater.

The homeowner can add more devices easily by placing new smart appliances and controlling them with similar buttons and LEDs showing their status.

You can create your own solution from this story in Python by representing each device as something that can be turned on or off, remembering its state, and showing the LED status with simple messages. This helps master concepts of grouping related data and actions together for easy control.
"""