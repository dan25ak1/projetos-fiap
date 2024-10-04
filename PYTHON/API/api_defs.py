from flask import Flask, jsonify, request

app = Flask(__name__)

#Aqui colocaremos nossas funcoes
@app.route("/Hello", methods=["GET"])
def hello():
    return "Ola mundo!"

@app.route("/Echo/<msg>", methods=["GET"])
def echo(msg):
    return msg






app.run (debug=True)