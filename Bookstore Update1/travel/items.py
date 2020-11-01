from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Item, Review
from .forms import *
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# create a blueprint
bp = Blueprint('item', __name__, url_prefix='/items')


# create a page that will show the details fo the item
@bp.route('/<id>')
def show(id):
    # item = get_item()
    item = Item.query.filter_by(id=id).first()
    cform = ReviewForm()  # create the review form and passit to render_template
    # in the html this is access as a varible named form
    return render_template('items/show.html', item=item, form=cform)


@bp.route('/<item>/review', methods=['GET', 'POST'])
@login_required #decorator between the route and view function 
def review(item):
    # here the form is created
    form = ReviewForm()
    item_obj = Item.query.filter_by(id=item).first()
    if form.validate_on_submit():  # this is true only in case of POST method
        review = Review(text=form.text.data,
                          item=item_obj, user=current_user)

        db.session.add(review)
        db.session.commit()
        print("Review posted by the user:", form.text.data)

    # in any case we go back to the same page.
    # notice the signature of url_for
    return redirect(url_for('item.show', id=item))


@bp.route('/create', methods=['GET', 'POST'])
@login_required #decorator between the route and view function 
def create():
    print('Method type: ', request.method)
    form = ItemForm()
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        item = Item(name=form.name.data,
                                  description=form.description.data,
                                  image=db_file_path,
                                  currency=form.currency.data,
                                  isbn=form.isbn.data,
                                  timeleft=form.timeleft.data)
        db.session.add(item)
        db.session.commit()

        print('Successfully created new travel item', 'Success')
        return redirect(url_for('item.create'))

    return render_template('items/create_item.html', form=form)

  # a new function
def check_upload_file(form):
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)

  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  db_upload_path='/static/image/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path


# http://127.0.0.1:5000
# http://127.0.0.1:5000/login

# http://127.0.0.1:5000/items/1

# http://127.0.0.1:5000/items/create
