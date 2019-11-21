POSTGRES_URL = "localhost"
POSTGRES_USER = "postgres"
POSTGRES_PW = "postgres"
POSTGRES_DB = "db_flask"


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
