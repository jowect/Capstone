import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
database_name = 'heroku_test'
user_name = 'postgres'
user_password = 'w1zu'
host = 'localhost:5432'
database_path = "postgres://{}:{}@{}/{}".format(
    user_name, user_password, host, database_name)

# for local db connection use database_path variable
# DATABASE_URL = database_path
DATABASE_URL = 'postgres://wqlwqncscphcfx:3e859ca1b5ec222029233138067b706303f74ac2c287d2a1d892bb086f8156ab@ec2-54-163-47-62.compute-1.amazonaws.com:5432/dvfahj6moq3cs'
os.getenv("{DATABASE_URL}")


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://wqlwqncscphcfx:3e859ca1b5ec222029233138067b706303f74ac2c287d2a1d892bb086f8156ab@ec2-54-163-47-62.compute-1.amazonaws.com:5432/dvfahj6moq3cs'
# SQLALCHEMY_DATABASE_URI = database_path
