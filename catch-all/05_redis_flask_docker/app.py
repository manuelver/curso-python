import requests
from flask import Flask, jsonify, request
from flask_caching import Cache


app = Flask(__name__)
app.config.from_object('config.BaseConfig')
cache = Cache(app)


@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
