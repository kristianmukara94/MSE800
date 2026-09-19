
from abc import ABC, abstractmethod


class Notifications (ABC):
 @abstractmethod    
 def send(self):
    pass


class Email(Notifications):
    def send(self):
       print("Send notifications")

class SMS(Notifications):
    def send(self):
        print("SMS notifications")

class Push(Notifications):
    def send(self):
        print("Push Notifications")

class NotificationFactory(ABC):
   @abstractmethod
   def create_notification (self):
      pass


class EmailFactory(NotificationFactory):
     def create_notification(self):
        return Email()
      

 