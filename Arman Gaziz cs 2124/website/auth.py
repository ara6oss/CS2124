from flask import Blueprint, render_template, request, flash
from .models import User
from . import db
from flask_login import login_user, current_user
#import cowsay,request

 
 
 






auth = Blueprint('auth', __name__)







@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        address = request.form.get('address')
        

        user = User.query.filter_by(address=address).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            new_user = User(address=address)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            #url = f"https://solana-gateway.moralis.io/nft/mainnet/{address}/metadata" 
            # headers = { 
 
#     "accept": "application/json", 
 
#     "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT" 
 
# } 
 
 
 
# response = requests.get(url, address=headers) 

    return render_template("login.html", user=current_user)
