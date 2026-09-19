from abc import ABC, abstractmethod

#Abstract Products

class Button(ABC):
    @abstractmethod
    def install(self) -> None:
        pass

class CheckBox(ABC):
    @abstractmethod
    def install(self) -> None:
        pass

#Concrete Products

class WindowsButton(Button):
    def install(self):
        print("Installing Windows button")

class WindowsCheckbox(CheckBox):
    def install(self):
        print("Installing Windows Checkbox")

class MacButton(Button):
    def install(self):
        print("Installing Mac button")

class MacCheckbox(CheckBox):
    def install(self):
        print("Install Mac Checkbox")

#AbstractFactory

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass

#concreteFactory

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> CheckBox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckbox()

#clientcode

class Client:

    def __init__(self, factory: GUIFactory):
        self.factory = factory 

    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()

        button.install()
        checkbox.install()


if __name__ == "__main__":
    windows_factory = WindowsFactory()
    client1 = Client(windows_factory)
    client1.create_ui()

    mac_factory = MacFactory()
    client2 = Client(mac_factory)
    client2.create_ui()