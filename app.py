from flask import render_template

from .tasks import response
from .model import User
from . import app


@app.route('/', methods=['GET'])
def index():
    # response.delay() фоновое не работает
    response()

    return render_template(
        "index.html",
        users=User.query.all()
    )
