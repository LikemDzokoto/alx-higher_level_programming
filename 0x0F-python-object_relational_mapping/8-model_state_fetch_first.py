/usr/bin/python3

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    import sys
    from model_state import Base, State

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                           @localhost:3306/{sys.argv[3]}")
    sess = Session(bind=engine)

    state = sess.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
