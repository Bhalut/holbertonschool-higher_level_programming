#!/usr/bin/python3
""" 10-model_state_my_get.py

    prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sys import argv as par
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = ("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()

    states = Session.query(State).filter(State.name == par[4]).first()

    if states:
        print(states.id)
    else:
        print('Not found')
    Session.close()


if __name__ == "__main__":
    main()