from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
    personas = [
        { "nombre" : "Abby" },
        { "nombre" : "Haider" }, 
        { "nombre" : "Daniel" },    
        { "nombre" : "Felipe" },    
        { "nombre" : "Mary" }   
    ]
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)