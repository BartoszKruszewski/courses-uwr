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
    data = request.get_json()
    if 'date' in data['properties']:
        data['properties']['date'] = date.fromisoformat(
            data['properties']['date'])
    db.session.add(models[data['model']](**data['properties']))
    db.session.commit()
    return jsonify({'message': 'Item created successfully'}), 201


@app.route('/api', methods=['GET'])
def get_all_items():
    data = request.get_json()
    items = models[data['model']].query.all()
    return jsonify([item.serialize() for item in items])


@app.route('/api', methods=['PUT'])
def update_item():
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
    data = request.get_json()
    item = models[data['model']].query.get(data['id'])
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
