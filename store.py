from products import Product


class Store(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            return self.products

    def remove_product(self,product):
        if product in self.products:
            self.products.remove(product)
            return self.products

    def get_total_quantity(self):
        lst_idx = 0
        item_quantity = 0
        while lst_idx < len(self.products):
            item_quantity += 1
            lst_idx += 1
        return item_quantity

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


