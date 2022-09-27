from flask import (Blueprint, render_template, request)
from . product_user_model import Product
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('base.html')
    # if request.method == 'GET':
    #     return render_template('base.html')
    # else: return render_template('base.html')

