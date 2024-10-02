from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'name': 'Starclouds',
        'version': '1.0',
        'description': 'Starbrains'
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
