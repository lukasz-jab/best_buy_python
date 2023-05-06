class Item:
    def __init__(self, name=None, model=None, price=None, link=None):
        self.name = name
        self.model = model
        self.price = price
        self.link = link

    def __repr__(self):
        return f"\n Item(name={self.name}, model={self.model}, price={self.price}, link={self.link})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.model == other.model

    # def __lt__(self, other):
    #     return float(self.price) < float(other.price)
