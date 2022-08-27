import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_IRO = 'sqlite:///' + os.path.join(basedir, 'app.db')
