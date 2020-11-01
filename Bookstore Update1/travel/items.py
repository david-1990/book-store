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
    cform = CommentForm()  # create the comment form and passit to render_template
    # in the html this is access as a varible named form
    return render_template('items/show.html', item=item, form=cform)


@bp.route('/<item>/comment', methods=['GET', 'POST'])
@login_required #decorator between the route and view function 
def comment(item):
    # here the form is created
    form = CommentForm()
    item_obj = Item.query.filter_by(id=item).first()
    if form.validate_on_submit():  # this is true only in case of POST method
        comment = Comment(text=form.text.data,
                          item=item_obj, user=current_user)

        db.session.add(comment)
        db.session.commit()
        print("Comment posted by the user:", form.text.data)

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


def get_item():
    # creating the description of Brazil
    b_desc = """Brazil is considered an advanced emerging economy.
    It has the ninth largest GDP in the world by nominal, and eight by PPP measures.
    It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    # an image location
    image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    item = Item('Brazil', b_desc, image_loc, '10 R$')
    # a comment
    comment = Comment(
        "User1", "Visited during the olympics, was great", '2019-11-12 11:00:00')
    item.set_comments(comment)
    return item


def get_item2():
    # creating the description of Brazil
    b_desc = """Since that place doesnt exist, heres a house which includes all amenities a human would need."""
    # an image location
    image_loc = 'https://fairmonthomes.com.au/images/facades_2019/DG41.jpg?Action=thumbnail&Width=256&Height=256&algorithm=fill_proportional'
    item = Item("Someone's house", b_desc, image_loc, '1 AUD$')
    # a comment
    comment = Comment("Tommy", "Wait, this is my house", '2020-09-2 2:00:00')
    item.set_comments(comment)
    return item

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
