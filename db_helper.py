from sqlalchemy import create_engine, MetaData
from sync import db


def create_tables():
    engine = create_engine("mysql+pymysql://root:wcg@127.0.0.1:3306/message", isolation_level='AUTOCOMMIT')

    meta = MetaData()
    meta.create_all(bind=engine, tables=[db.msg])


if __name__ == '__main__':
    create_tables()
