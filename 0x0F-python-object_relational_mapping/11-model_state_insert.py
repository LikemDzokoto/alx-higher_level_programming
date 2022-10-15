#!/usr/bin/python3


if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    import sys
    from model_state import Base, State

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                           @localhost:3306/{sys.argv[3]}")
    session = Session(bind=engine)
    newRec = State(name="Louisiana")
    session.add(newRec)
    session.commit()

    # now print its ID
    res = session.query(State).filter(State.name == "Louisiana")

    if len(res.all()) > 0:
        print(res[0].id)
    else:
        print("Not found")
