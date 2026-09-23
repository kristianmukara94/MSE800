from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, price: float):
        pass


class Investor(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, price: float):
        print(f"{self.name} received stock price update: {price}")

class Stock:
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self._price = price
        self._observers: list[Observer] = []

    @property
    def price(self) -> float:   
        return self._price

    @price.setter
    def price(self, new_price: float):
        if self._price != new_price:    
            self._price = new_price
            self.notify_investors()

    def register_investor(self, investor: Observer):
        self._observers.append(investor)

    def unregister_investor(self, investor: Observer):
        self._observers.remove(investor)

    def notify_investors(self):
        for observer in self._observers:
            observer.update(self._price)


    if __name__ == "__main__":
        tech_stock = Stock("TECH", 100.0)

        ali = Investor("Ali")
        sara = Investor("Sara")

        tech_stock.register_investor(ali)
        tech_stock.register_investor(sara)


        print("Changing stock price to 105.0")
        tech_stock.price = 105.0

        print("Changing stock price to 112.5")
        tech_stock.price = 112.5
