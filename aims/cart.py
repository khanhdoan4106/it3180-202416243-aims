MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            return True
        return False

    def total_cost(self):
        return round(sum(d.cost for d in self.items), 2)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("*********************** CART ***********************")
        for i, dvd in enumerate(self.items, 1):
            print(f"{i}. DVD - {dvd.title} - {dvd.category} - "
                  f"{dvd.director} - {dvd.length}: {dvd.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("****************************************************")