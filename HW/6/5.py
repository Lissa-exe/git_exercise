import json

def answer(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for idx, q in enumerate(data.get('questions', [])):
        data['questions'][idx]['answer'] = input(q['q'])

    with open(file_path, 'w') as file:
        json.dump(data, file)

answer('questions.json')