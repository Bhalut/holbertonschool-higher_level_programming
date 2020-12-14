#!/usr/bin/python3
""" 9-model_state_filter_a.py

    lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa.
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

    states = Sess.query(State).filter(State.name.contains('a'))
    states = states.order_by(State.id)

    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == "__main__":
    main()
