from flask import Flask, render_template
from . import app
from .tasks import response


@app.route('/', methods=['GET'])
def index():
    return render_template(
        "index.html",
        users=response(),
    )
