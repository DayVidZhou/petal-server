import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'petal.db')
    #'postgres://jtydqcrurjiuyx:77c218e3044bfc940254ec497dd1cd1b81b6b6cf6365e50836265f2d16fdf941@ec2-174-129-236-21.compute-1.amazonaws.com:5432/d7sq66opjuee77'
    SQLALCHEMY_TRACK_MODIFICATIONS = False