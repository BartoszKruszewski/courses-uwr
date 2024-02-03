"""
Flask API Script

This script defines a simple Flask API for performing CRUD operations on different models.
It interacts with a SQLite database using SQLAlchemy.

Endpoints:
    - POST /api: Create a new item for a specified model.
    - GET /api: Retrieve all items for a specified model.
    - PUT /api: Update an existing item for a specified model.
    - DELETE /api: Delete an existing item for a specified model.

Usage:
    Run the script to start the Flask application. The API will be accessible at http://127.0.0.1:5000/api

Dependencies:
    - Flask: for building the web application
    - SQLAlchemy: for interacting with the database
    - models.py: contains the database models
    - datetime: for handling date conversions

"""

from flask import Flask, request, jsonify
from models import models, db
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/api', methods=['POST'])
def create_item():
    """
    Endpoint to create a new item for a specified model.

    Request JSON Format:
    {
        "model": "model_name",
        "properties": {
            "property1": "value1",
            "property2": "value2",
            ...
        }
    }

    Returns:
    JSON response with a success message and HTTP status code 201.

    """
    data = request.get_json()
    if 'date' in data['properties']:
        data['properties']['date'] = date.fromisoformat(
            data['properties']['date'])
    db.session.add(models[data['model']](**data['properties']))
    db.session.commit()
    return jsonify({'message': 'Item created successfully'}), 201


@app.route('/api', methods=['GET'])
def get_all_items():
    """
    Endpoint to retrieve all items for a specified model.

    Request JSON Format:
    {
        "model": "model_name"
    }

    Returns:
    JSON response with a list of serialized items and HTTP status code 200.

    """
    data = request.get_json()
    items = models[data['model']].query.all()
    return jsonify([item.serialize() for item in items])


@app.route('/api', methods=['PUT'])
def update_item():
    """
    Endpoint to update an existing item for a specified model.

    Request JSON Format:
    {
        "model": "model_name",
        "id": item_id,
        "properties": {
            "property1": "new_value1",
            "property2": "new_value2",
            ...
        }
    }

    Returns:
    JSON response with a success message and HTTP status code 200.
    If the item is not found, returns a JSON response with an error message and HTTP status code 404.

    """
    data = request.get_json()
    if 'date' in data['properties']:
        data['properties']['date'] = date.fromisoformat(
            data['properties']['date'])
    item = models[data['model']].query.get(data['id'])
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    for key, value in data['properties'].items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})


@app.route('/api', methods=['DELETE'])
def delete_item():
    """
    Endpoint to delete an existing item for a specified model.

    Request JSON Format:
    {
        "model": "model_name",
        "id": item_id
    }

    Returns:
    JSON response with a success message and HTTP status code 200.
    If the item is not found, returns a JSON response with an error message and HTTP status code 404.

    """
    data = request.get_json()
    item = models[data['model']].query.get(data['id'])
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})


def run():
    app.run(debug=True)
