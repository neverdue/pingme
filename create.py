import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine('postgres://oyeubcfprgkknv:61c161ce0a9f0a2591792d4443083dd3f8e5e24ff3c68ca012b456698623c84e@ec2-34-193-117-204.compute-1.amazonaws.com:5432/d880fut9ik2j31', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)
