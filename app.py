from flask import Flask
from config.database import init_db
from routes.user_routes import user_routes

app = Flask(__name__)

app.secret_key = 'secret_key'


# Initialize MongoDB
init_db(app)


# Register user routes
app.register_blueprint(user_routes)


# Home
@app.route('/')
def hello():

    return "Hello"


# Run Flask
if __name__ == '__main__':
    app.run(debug=True)