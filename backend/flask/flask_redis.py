from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/set/<key>/<value>')
def set_value(key, value):
    cache.set(key, value)
    return f'{key} set to {value}'

@app.route('/get/<key>')
def get_value(key):
    value = cache.get(key)
    if value:
        return value.decode('utf-8')
    return 'Key not found.'

if __name__ == '__main__':
    app.run(debug=True)
