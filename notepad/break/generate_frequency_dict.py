import requests
import json


def generate_frequency_dict():
    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
    response = requests.get('http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml')
    arr = [i.lower() for i in response.text if i.lower() in alphabet]

    d: dict = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1

    with open('freq.json', 'w', encoding='UTF-8') as file:
        json.dump(d, file, ensure_ascii=False)


def generate_list_for_frequency_analyse():
    with open('freq.json', encoding='UTF-8') as file:
        d = json.load(file)

        return [element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)]


print(generate_list_for_frequency_analyse())