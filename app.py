from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

class MushroomForm(Form):
    cap_shape = StringField('Cap shape')
    cap_surface = StringField('Cap surface')
    cap_color = StringField('Cap color')          
    bruises = StringField('Bruises')     
    odor = StringField('Odor')     
    gill_attachment = StringField('')     
    gill_spacing = StringField('Gill spacing')     
    gill_color = StringField('Gill color')     
    stalk_shape = StringField('Stalk shape')       
    stalk_surface_above_the_ring= StringField('Stalk surface above the ring')     
    stalk_surface_below_the_ring= StringField('Stalk surface below the ring')     
    stalk_color_above_the_ring= StringField('Stalk color above the ring')     
    stalk_color_below_the_ring= StringField('Stalk color below the ring')     
    veil_type= StringField('Veil type')     
    veil_color = StringField('Veil color')     
    ring_number = StringField('Ring number')     
    spore_print_color= StringField('Spore print color')     
    population = StringField('Population')   
    habitat = StringField('Habitat')   

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = requestForm(request.form)
    if request.method == 'POST':
        
        return render_template('result.html')
    else:
        return render_template('predict.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create de cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash("You are now registerd and can log in", 'success')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)   

if  __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

