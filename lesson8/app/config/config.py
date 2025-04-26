import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'segredo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
