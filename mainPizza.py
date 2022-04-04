from pizzaproducer import PizzaProvider
from faker import Faker

fake = Faker()

fake.add_provider(PizzaProvider)
for i in range(0,10):
    print(fake.pizza_name())