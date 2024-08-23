from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
    personas = ["Abby", "Haider", "Daniel", "Felipe", "Mary"]
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)