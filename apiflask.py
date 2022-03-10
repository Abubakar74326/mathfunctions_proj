# from typing import Optional
# from fastapi import FastAPI

from flask import Flask
import allfunctions

app = Flask(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.route("/function/<int:num>/")  # math/
def read_item(num: int):  # math_func
    object = allfunctions.Mathematics(int(num))
    results = {
        "number": int(num),
        "factorial": object.factorial(),
        "square": object.square(),
        "cube": object.cube(),
    }
    return str(results)
