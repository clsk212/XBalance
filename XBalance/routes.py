from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "¡Hola, bienvenido a XBalance!"
