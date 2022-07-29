class Consumption:
    def __init__(self, fuel_used: float, traveled_dist: float, price: float):
        self.price = price
        self.traveled_dist = traveled_dist
        self.fuel_used = fuel_used

    def consumption(self):
        return self.fuel_used / self.traveled_dist * 100

    def cost(self):
        return self.price * self.consumption() / 100


c = Consumption(40, 250, 49.5)

print(f'consumption is {c.consumption()} km/h')
print(f'price per 1km: {c.cost()} RUB')
print(f"price per 100km:{c.cost() * 100} RUB")
