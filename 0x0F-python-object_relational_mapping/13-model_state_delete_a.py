#!/usr/bin/python3
''' script that deletes all object with name containing 'a' '''


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                             @localhost:3306/{sys.argv[3]}")
    session = Session(bind=engine)

    '''states_with_a = session.query(State).filter(
    State.name.like("%a%")).all()
    for record in states_with_a:
        session.delete(record)'''
    session.query(State).filter(
      State.name.like("%a%")
    ).delete(synchronize_session='fetch')
    session.commit()
