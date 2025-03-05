from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:12345@127.0.0.1:3306/todoapplicationdatabase'
SQLALCHEMY_DATABASE_URL = 'postgresql://deploy_server_user:TdFNtEZzY8zVQbmZCAz4JnILMgdozRh3@dpg-cv3rn8qj1k6c73crc6dg-a.oregon-postgres.render.com/deploy_server'


engine =  create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =  sessionmaker(autocommit = False,autoflush=False,bind=engine)

Base = declarative_base()

