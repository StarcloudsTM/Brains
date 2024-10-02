from flask import Flask, Blueprint

app = Flask(__name__)
user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def get_users():
    return 'List of users'

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
