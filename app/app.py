from flask import Flask, render_template, Blueprint
from .forms import NameForm
from .models import Name
from . import db

bp = Blueprint('app', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()

    if form.validate_on_submit():
        db.session.add(Name(name=form.name.data))
        db.session.commit()
        names = Name.query.all()
        return render_template('index.html', form=form, names=names)
    names = Name.query.all()
    return render_template('index.html', form=form, names=names)

if __name__ == '__main__':
    app.run(debug=True)
