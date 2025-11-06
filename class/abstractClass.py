from abc import ABC, abstractmethod

class Payment(ABC):   # Inherit from ABC

    @abstractmethod
    def pay(self, amount):
        pass  # No body — subclasses must define it

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def temp(self):
        pass

    # def pay(self, amount):
    #     print(f"Paid {amount} using PayPal.")

# Cannot instantiate abstract class
# payment = Payment()  # ❌ TypeError

# Valid — subclasses implemented the abstract method
card = CreditCardPayment()
card.pay(100)

paypal = PayPalPayment()
paypal.pay(200)

"""
An abstract class is a blueprint for other classes.
It defines a set of methods and properties that a child class must have, but it doesn’t necessarily tell how they should behave.

In practice:

You never create (or instantiate) an abstract class directly.

Instead, you inherit from it and implement any abstract methods in your subclass."""