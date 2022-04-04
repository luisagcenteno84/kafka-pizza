from faker import Faker
import random

fake = Faker()

max_pizzas_in_order = 5
max_toppings_in_pizza=3

def pizza_topping(self):
    available_pizza_toppings = [
        'tomato',
        'mozzarella',
        'blue cheese',
        'salami',
        'green peppers',
        'ham',
        'olives',
        'anchovies',
        'artichokes',
        'olives',
        'garlic',
        'tuna',
        'onion',
        'pineapple',
        'strawberry',
        'banana'
    ]
    return random.choice(available_pizza_toppings)

def pizza_shop(self):
    pizza_shops = [
        'Marios Pizza',
        'Luigis Pizza',
        'Circular Pi Pizzeria',
        'Ill Make You a Pizza You Can''t Refuse',
        'Mammamia Pizza',
        'Its-a me! Mario Pizza!'
    ]
    return random.choice(pizza_shops)

def produce_pizza_producer(orderid = 1):
    shop = fake.pizza_shop()

    pizzas = []
    for pizza in range(random.randint(1,max_pizzas_in_order)):
        toppings = []
        for topping in range(random.randint(1,max_toppings_in_pizza)):
            toppings.append(fake.pizza_topping())
        pizza.append({
            'pizzaName': fake.pizza_name(),
            'additionalToppings': toppings
        })

    key = shop
    
    message = {
        'id': orderid,
        'shop': shop,
        'name': fake.unique.name(),
        'phoneNumber': fake.unique.phoneNumber(),
        'address': fake.address(),
        'pizzas': pizzas
    }

    return message, key