class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price

  def discount_price(self):
      return 0.9 * self.sticker_price

class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.options = {"SportWheels": False, "SportEngine": False, "SportInterior": False}

  def add_option(self, option):
      if option in self.options:
          self.options[option] = True

  def pricewithoptions(self):
      updated_price = self.discount_price()

      for option, selected in self.options.items():
          if selected:
              option_price = self.get_option_price(option)
              updated_price += option_price

      return updated_price

  def get_option_price(self, option):
      option_prices = {"SportWheels": 1000.00, "SportEngine": 3000.00, "SportInterior": 2000.00}
      return option_prices.get(option, 0.00)

sport_car = Sport("Toyota", "Supra", 50000)
sport_car.add_option("SportWheels")
sport_car.add_option("SportEngine")
sport_car.add_option("SportInterior")

print(f"{sport_car.make} {sport_car.model} Price with Options: ${sport_car.pricewithoptions()}")
