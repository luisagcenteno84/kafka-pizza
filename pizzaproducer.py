import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        validPizzaNames = ['Margherita',
                            'Marinara',
                            'Diavola',
                            'Mari & Monti',
                            'Salami',
                            'Pepperoni'
        ]
        return validPizzaNames[random.randint(0,len(validPizzaNames)-1)]
