import os

# Superset is a big system needs its own db to remember which graphs we created, which useres we have, and what are their roles.
# In building the Postgres db (init.sql), we created two db. telephony_db and superset_db.
# That's exactly The reason. We want to seperate the data we want to analyze (telephony_db) and the data that superset needs to run (superset_db).

#SECRET_KEY is used to encrypt session cookies and other security related needs by Flask. 
# It should be set to a long random string in production, and kept secret. 
# You can generate a random string using Python's os.urandom function, for example: os.urandom(24).hex().
SECRET_KEY = '' 

# SQLALCHEMY_DATABASE_URI is the connection string for your database. It should be in the format:
# dialect+driver://username:password@host:port/database
# For example, for a PostgreSQL database, it might look like:
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost:5432/mydatabase'
SQLALCHEMY_DATABASE_URI = ''
# BABEL_DEFAULT_LOCALE and WTF_CRSF_ENABLED are used for internationalization and security in Flask applications.
BABEL_DEFAULT_LOCALE = 'en'

WTF_CRSF_ENABLED = False
