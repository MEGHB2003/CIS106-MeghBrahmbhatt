class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

class Manager(Employee):
  def long_term_bonus(self):
      return 0.4 * self.salary

manager = Manager("John Doe", 50000)
print(f"{manager.name}'s Long Term Bonus: ${manager.long_term_bonus()}")
