import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonacci():
    fibo = '0, 1'
    i = 1
    limite = 50
    anterior = 0
    proximo = 1
    while i < limite:
        novo = anterior + proximo
        anterior = proximo
        proximo = novo
        i = i + 1
        fibo+= ',' + str(novo)

    return fibo

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

