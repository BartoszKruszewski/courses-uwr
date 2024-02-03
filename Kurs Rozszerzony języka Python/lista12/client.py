import requests
import argparse

API_URL = "http://127.0.0.1:5000/api"


def get(model):
    data = {"model": model}
    response = requests.get(API_URL, json=data)
    return response.json()


def create(model, properties):
    data = {"model": model, "properties": properties}
    response = requests.post(API_URL, json=data)
    return response.json()


def update(model, id, properties):
    data = {"model": model, "id": id, "properties": properties}
    response = requests.put(API_URL, json=data)
    return response.json()


def delete(model, id):
    data = {"model": model, "id": id}
    response = requests.delete(API_URL, json=data)
    return response.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Database client')

    ARGUMENTS = {
        'artist': ['name'],
        'album': ['title', 'date', 'artist_id'],
        'song': ['title', 'album_id'],
    }

    parser.add_argument('model', type=str, help='Table name')
    parser.add_argument(
        'operation', type=str, help='Operation type',
        choices=['get', 'create', 'update', 'delete']
    )
    parser.add_argument('--id', type=int, help='ID of item')
    args, remaining_args = parser.parse_known_args()
    model = args.model
    operation = args.operation
    id = args.id

    dynamic_parser = argparse.ArgumentParser(
        description='Your description for dynamic arguments here')

    for arg_name in ARGUMENTS[model]:
        dynamic_parser.add_argument(f'--{arg_name}', type=str)

    args = dynamic_parser.parse_args(remaining_args)

    match operation:
        case 'get':
            print(get(model))
        case 'create':
            print(create(model, {
                arg_name: getattr(args, arg_name)
                for arg_name in ARGUMENTS[model]}
            ))
        case 'update':
            print(update(model, id, {
                arg_name: getattr(args, arg_name)
                for arg_name in ARGUMENTS[model]}
            ))
        case 'delete':
            print(create(model, id))
