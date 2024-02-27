"""
Redirecciona a una URL a partir de un código
"""

import os
from flask import Flask, redirect
import json

app = Flask(__name__)


@app.route('/<string:codigo>')
def redireccion(codigo: str):

    data = []

    with open('codigos.json', 'r') as f:

        data = json.load(f)

    r = list(filter(lambda x: x['codigo'] == codigo, data))

    if r:
        return redirect(r[0]['redireccion'], code=302)

    return {
        'message': 'Código no encontrado'
    }

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
