import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)
response_json = json.loads(response.text)

for i, class_data in enumerate(response_json['results']):
    print(f"{i + 1}. {class_data['name']}")

seleccion = int(input("Escoge un personaje: ")) - 1

selected_class_name = response_json['results'][seleccion]['name'].lower()

class_url = f"{URI}/{selected_class_name}"
response = requests.get(class_url)
class_data = json.loads(response.text)


proficiencies = class_data.get('proficiencies', [])


if proficiencies:
    print(f"Proficiencias de la clase {class_data['name']}:")
    for i, proficiency in enumerate(proficiencies):
        print(f"{i + 1}. {proficiency['name']}")
else:
    print(f"La clase {class_data['name']} no tiene proficiencias especificadas.")
