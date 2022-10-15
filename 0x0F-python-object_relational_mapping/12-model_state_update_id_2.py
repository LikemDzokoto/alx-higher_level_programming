#!/usr/bin/python3
''' change an object's name when provided ID '''



if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                             @localhost:3306/{sys.argv[3]}")
    session = Session(bind=engine)
    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
