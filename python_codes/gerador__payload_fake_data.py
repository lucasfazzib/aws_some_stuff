import random
import string
import uuid
from faker import Faker
import boto3
import json


#ajustar quantas msgs...
NUM_MESSAGES = 10
FILE_NAME = "messages.json"

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


def generate_random_number(length):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))


def gerar_json_aleatorio():
    fake = Faker("pt_BR")
    name = fake.name()
    json_data = {
        "canal": 9415,
        "codigo_data": 20809,
        "cliente": {
            "numero": generate_random_number(12),
            "pessoal": {
                "id_dev": str(uuid.uuid4()),
                "name": "testes dev",
                "email": fake.email(),
                "nome_cliente": name,
                "username": fake.user_name(),
                "social_name": name,
                "endereco": [
                    {
                        "cep": generate_random_number(7),
                        "endereco": fake.street_name(),
                        "numero": fake.building_number(),
                        "bairro": fake.neighborhood(),
                        "cidade": fake.city(),
                        "estado": fake.state(),
                        "country": fake.country(),
                        "phones": [
                            {
                                "phone_type": "RESIDENTIAL",
                                "phone": fake.phone_number(),
                                "extension": fake.phone_number()[1:3]
                            }
                        ]
                    }
                ]
            },
            "conta_teste": {
                "id_dev": str(uuid.uuid4())
            },
            "identificacao": {
                "id": str(uuid.uuid1())
            }
        }
    }

    return json_data


with open(FILE_NAME, 'w') as file:
    for i in range(NUM_MESSAGES):
        json_data = gerar_json_aleatorio()
        json.dump(json_data, file)
        if i < NUM_MESSAGES - 1:
            file.write(',')
        file.write('\n')