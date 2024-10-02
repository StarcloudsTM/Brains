from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/login', methods=['POST'])
def login():
    auth_data = request.get_json()
    if auth_data['username'] == 'admin' and auth_data['password'] == 'password':
        token = jwt.encode({'user': 'admin', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return 'Invalid credentials.'

if __name__ == '__main__':
    app.run(debug=True)
