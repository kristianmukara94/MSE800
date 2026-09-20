
from abc import abstractmethod


class Target:
    @abstractmethod
    def pay(self,amount):
     pass

class OldPaymemtSystem:

   def make_payment(self,amount):
     print(f"Payment of ${amount} made using the old payment system")

class PaymentAdapter(Target):

    def __init__(self, OldPaymentSystem):
        self.OldPaymentSystem = OldPaymentSystem

    def pay(self, amount):
        self.OldPaymentSystem.make_payment(amount    )

adaptee = OldPaymemtSystem()
adapter = PaymentAdapter(adaptee)
adapter.pay(500)
