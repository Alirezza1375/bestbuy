import products


class Store:
    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        """
        Adds a product to store
        :param product:
        """
        return self.products_list.append(product)

    def remove_product(self, product):
        """
        Removes product from store
        :param product:
        """
        if product in self.products_list:
            return self.products_list.remove(product)

    def get_total_quantity(self):
        """
        Returns how many items are in the store in total.
        """
        return sum(product.get_quantity() for product in self.products_list)

    def get_all_products(self):
        """
        Returns all products in the store that are active.
        """
        return [product for product in self.products_list if product.is_active()]

    def order(self, shopping_list):
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.

        :param shopping_list:
         """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
            self.get_total_quantity -= quantity
        return f"Total cost: {total_price} dollars."


product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = Store(product_list)
print(best_buy.get_all_products())