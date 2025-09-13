from flask import Flask, jsonify
from flask_jwt_extended import create_access_token, JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production! Replace with secure secret key management.
jwt = JWTManager(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create database tables
with app.app_context():
    db.create_all()

# API routes
@app.route('/api/login', methods=['POST'])
def login():
    username = 'testuser'  # Replace with actual login logic
    password = 'testpassword'  # Replace with secure password handling in production
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/api/report')
def generate_report():
    return "Report generated"  # Replace with actual report generation logic

@app.route('/')
def hello_world():
    return 'Hello, SecPro!'

# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SecPro"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Set debug=False in production
