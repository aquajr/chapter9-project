from app import app
from flask import render_template, flash,redirect
from app.forms import RegisterForm, AddProductForm

@app.route('/')
@app.route('/shop')
def index():
    return render_template('index.html', title='Shop')


@app.route('/register', methods=['GET','POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been registered')
        return redirect('/shop')
    return render_template('register.html', title='Register', form=form)


@app.route('/add-product', methods=['GET','POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'Your product has been added')
        return redirect('/shop')
    return render_template('add_product.html', title='Add product', form=form)