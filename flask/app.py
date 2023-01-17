from flask import Response, Flask

app = Flask(__name__)


@app.post("/users")
def add_user() -> Response:
    print(request.json)
    return Response(status=501)

@app.post("/users/")
def get_user() -> Response:
    print(request.json)
    return Response(status=200)