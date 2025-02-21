from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime
from storage import MemStorage
from models import Entry, EntrySchema, UserSchema

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'your-secret-key'  # In production, use a secure secret key

login_manager = LoginManager()
login_manager.init_app(app)

# Initialize storage
storage = MemStorage()
entry_schema = EntrySchema()
user_schema = UserSchema()

@login_manager.user_loader
def load_user(user_id):
    return storage.get_user(int(user_id))

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = storage.create_user(data['username'], data['password'])
        login_user(user)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = storage.verify_user(data['username'], data['password'])
    if user:
        login_user(user)
        return jsonify(user.to_dict())
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    logout_user()
    return '', 200

@app.route('/api/user', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict())
    return '', 401

@app.route('/api/entries', methods=['GET'])
@login_required
def get_entries():
    entries = storage.get_entries_by_user(current_user.id)
    return jsonify([entry.to_dict() for entry in entries])

@app.route('/api/entries/date/<date>', methods=['GET'])
@login_required
def get_entries_by_date(date):
    try:
        # Parse the date from the URL parameter
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        entries = storage.get_entries_by_date(date_obj, current_user.id)
        # Ensure we're returning serialized entries
        return jsonify([entry.to_dict() for entry in entries])
    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400

@app.route('/api/entries', methods=['POST'])
@login_required
def create_entry():
    data = request.get_json()

    try:
        # Validate and create the entry
        entry_data = entry_schema.load(data)
        entry_data['user_id'] = current_user.id
        entry = Entry(**entry_data)
        created_entry = storage.create_entry(entry)
        # Return the serialized entry
        return jsonify(created_entry.to_dict())
    except Exception as e:
        print(f"Error creating entry: {str(e)}")  # Add logging
        return jsonify({'message': str(e)}), 400

@app.route('/api/entries/<int:entry_id>', methods=['PATCH'])
@login_required
def update_entry(entry_id):
    data = request.get_json()
    try:
        updated_entry = storage.update_entry(entry_id, data)
        if updated_entry.user_id != current_user.id:
            return jsonify({'message': 'Unauthorized'}), 403
        return jsonify(updated_entry.to_dict())
    except KeyError:
        return jsonify({'message': 'Entry not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/api/search', methods=['GET'])
@login_required
def search_entries():
    query = request.args.get('q')
    if not query:
        return jsonify({'message': 'Search query required'}), 400

    results = storage.search_entries(query, current_user.id)
    return jsonify([entry.to_dict() for entry in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)