class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if self.name == "" or self.price < 0 or self.quantity < 0:
            raise Exception("Something went wrong!")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if self.quantity == 0 and quantity == self.quantity:
            self.active = False
            return
        else:
            self.quantity = quantity
            return

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity == 0 or quantity > self.quantity or not self.active:
            raise ValueError("Something went wrong!!")
        else:
            self.quantity -= quantity
            return f"Total price: {float(self.price * quantity)}"












