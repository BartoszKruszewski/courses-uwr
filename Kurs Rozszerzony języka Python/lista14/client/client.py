"""
Database Client Script

This script provides a command-line interface to interact with a database API.
It supports basic CRUD operations (Create, Read, Update, Delete) for different models.

Usage:
    python script.py <model> <operation> [--id <id>] [--<property_name> <property_value>]

Example:
    python script.py artist get
    python script.py album create --title "Album Title" --date "2023-01-01" --artist_id 1
    python script.py song update --id 5 --title "New Title" --album_id 2

Dependencies:
    - requests: for making HTTP requests

"""

from requests import get as req_get, post as req_post, \
    put as req_put, delete as req_delete
import argparse
from typing import Dict, Union

API_URL = "http://127.0.0.1:5000/api"
USERNAME = 'user1'
PASSWORD = 'password1'

def get(model: str) -> Dict[str, Union[str, int]]:
    """
    Retrieve data for the specified model.

    Args:
        model (str): The name of the model/table.

    Returns:
        Dict[str, Union[str, int]]: The JSON response containing model data.

    """
    data = {"model": model, 'username': USERNAME, 'password': PASSWORD}
    response = req_get(API_URL, json=data)
    return response.json()


def create(
        model: str, properties: Dict[str, Union[str, int]]
        ) -> Dict[str, Union[str, int]]:
    """
    Create a new entry for the specified model with the given properties.

    Args:
        model (str): The name of the model/table.
        properties (Dict[str, Union[str, int]]): The properties of the new entry.

    Returns:
        Dict[str, Union[str, int]]: The JSON response containing the created entry.

    """
    data = {
        "model": model, "properties": properties,
        'username': USERNAME, 'password': PASSWORD}
    response = req_post(API_URL, json=data)
    return response.json()


def update(
        model: str, id: int, properties: Dict[str, Union[str, int]]
        ) -> Dict[str, Union[str, int]]:
    """
    Update an entry for the specified model with the given ID and properties.

    Args:
        model (str): The name of the model/table.
        id (int): The ID of the entry to be updated.
        properties (Dict[str, Union[str, int]]): The properties to update.

    Returns:
        Dict[str, Union[str, int]]: The JSON response containing the updated entry.

    """
    data = {"model": model, "id": id, "properties": properties,
             'username': USERNAME, 'password': PASSWORD}
    response = req_put(API_URL, json=data)
    return response.json()


def delete(model: str, id: int) -> Dict[str, Union[str, int]]:
    """
    Delete an entry for the specified model with the given ID.

    Args:
        model (str): The name of the model/table.
        id (int): The ID of the entry to be deleted.

    Returns:
        Dict[str, Union[str, int]]: The JSON response confirming the deletion.

    """
    data = {"model": model, "id": id,
             'username': USERNAME, 'password': PASSWORD}
    response = req_delete(API_URL, json=data)
    return response.json()

def run():
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
        description='Dynamic arguments for model properties')

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
            print(delete(model, id))
