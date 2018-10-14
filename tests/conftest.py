import pytest
from app import create_app
from app.models import Name
from app import db


@pytest.fixture(scope='module')
def new_name():
    name = Name(name='Mark')
    return name


@pytest.yield_fixture(scope='module')
def test_client():
    app = create_app('testing')
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.yield_fixture(scope='module')
def create_database():
    db.create_all()
    name = Name(name='Mark')
    db.session.add(name)
    db.session.commit()
    yield db
    db.session.close()
    db.drop_all()
