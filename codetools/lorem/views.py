from django.shortcuts import render
from faker import Faker
import faker


def lorem_ipsum(request):
    fake = Faker('pt_BR')
    ipsum = []
    for i in range(2):
        ipsum.append(fake.paragraph(nb_sentences=10))

    context = {
        "name": fake.name(),
        "job": fake.job(),
        "address": fake.address(),
        "placa": fake.license_plate(),
        "uf": fake.estado(),
        "cpf": fake.cpf(),
        "color": fake.hex_color(),
        "ipsum": ipsum,
    }
    return render(request, "lorem-ipsum.html", context=context)