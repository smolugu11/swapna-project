class Camera:
    def take_phone(self):
        print("Taking photo")
class Phone:
    def make_call(self):
        print("Making call")
class SmartPhone(Camera,Phone): # multiple inheritance
    pass
def main():
    s1 = SmartPhone()
    s1.take_phone()
    s1.make_call()

main()