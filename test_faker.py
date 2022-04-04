from faker import Faker
faker = Faker('es_MX')

message = {
    'name': faker.name(),
    'address': faker.address(),
    'phone': faker.phone_number()
}

print(message)