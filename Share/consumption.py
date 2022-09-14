# My first script for calculate the automobile consumption and price per km
# it important for me, because in my car don't have an on-board computer
class Consumption:
    def __init__(self, fuel_used: float, traveled_dist: float, price: float):
        self.price = price
        self.traveled_dist = traveled_dist
        self.fuel_used = fuel_used

    def consumption(self):
        return self.fuel_used / self.traveled_dist * 100

    def cost(self):
        return self.price * self.consumption() / 100


if __name__ == '__main__':
    p = float(input('Price per liter: '))
    t_dist = float(input('Traveled distance: '))
    f_used = float(input('Used fuel: '))
    c = Consumption(f_used, t_dist, p)

    print(f'consumption is {c.consumption()} km/h')
    print(f'price per 1km: {c.cost()} RUB')
    print(f"price per 100km:{c.cost() * 100} RUB")
