import io
import json
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, resolve_url
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import base64

def lorem_ipsum(request):
    fake = Faker('pt_BR')
    ipsum = []
    for i in range(2):
        ipsum.append(fake.paragraph(nb_sentences=10))

    with open(f"{settings.BASE_DIR}/codetools/lorem/json/lorem_ipsum.json") as db_json:
        links_uteis = json.loads(db_json.read())

    context = {
        "name": fake.name(),
        "job": fake.job(),
        "address": fake.address(),
        "placa": fake.license_plate(),
        "uf": fake.estado(),
        "cpf": fake.cpf(),
        "color": fake.hex_color(),
        "ipsum": ipsum,
        "links_uteis": links_uteis,
    }

    return render(request, "lorem-ipsum.html", context=context)

def lorem_pixel(request):

    width = int(request.GET.get("width", 1280))
    height = int(request.GET.get("height", 720))
    base64_response = request.GET.get("base64", False)

    color = request.GET.get("color", "#cccccc")

    img = Image.new('RGB', (width, height), color = color)
    draw = ImageDraw.Draw(img)

    font_path = f"{settings.BASE_DIR}/contrib/roboto.ttf"
    
    font = ImageFont.truetype(font_path, 30)
    font_2 = ImageFont.truetype(font_path, 18)
    
    mark = f"Codetools {settings.APP_VERSION}"
    
    draw.text((20, 20),mark,(255,255,255), font=font)
    draw.text((20, 50),"codetools.com.br",(255,255,255), font=font_2)

    output = io.BytesIO()

    img.save(output, format='PNG')

    if base64_response:
        base_image = base64.b64encode(output.getvalue()).decode()
        resposta = dict(base64_img=f"data:image/png;base64,{base_image}", filename="loren_pixel.png")
        response = JsonResponse(resposta)
    else:
        response = HttpResponse(output.getvalue(), content_type='image/png')
        response['Content-Disposition'] = 'filename="loren_pixel.png"'

    return response

def lorem_pixel_index(request):

    with open(f"{settings.BASE_DIR}/codetools/lorem/json/lorem_pixel.json") as db_json:
        links_uteis = json.loads(db_json.read())

    context = {
        "links_uteis": links_uteis,
    }
    
    return render(request, "lorem-pixel.html", context)