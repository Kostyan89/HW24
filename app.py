import os

from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest

from functions import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Response:
    try:
        file_name = request.args["file_name"]
        cmd1 = request.args["cmd1"]
        value1 = request.args["value1"]
        cmd2 = request.args["cmd2"]
        value2 = request.args["value2"]
    except KeyError:
        raise BadRequest

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return Response(f"{file_name} not found")

    with open (file_path, "r") as f:
        res = build_query(f, cmd1, value1, cmd2, value2)
        content = '\n'.join(res)
    return app.response_class(content, content_type="text/plain")
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py

