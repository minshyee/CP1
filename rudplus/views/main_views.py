
from flask import Blueprint, render_template, request

main_bp = Blueprint('main',__name__)

# home
@main_bp.route('/')
def home():
    return render_template('main.html')

# 입력 페이지
@main_bp.route('/input', methods=['GET'])
def input():
    # Get method
    if request.method == 'GET':
        return render_template('input.html')


# 결과페이지
@main_bp.route('/predict', methods=['POST'])
def predict():

    # predic model
    pred = 23
    # keyword model
    key1='life'
    key2='life'
    key3='life'
    key4='life'
    key5='life'

    return render_template('result.html', result = pred, key1=key1,key2=key2,key3=key3,key4=key4,key5=key5)
