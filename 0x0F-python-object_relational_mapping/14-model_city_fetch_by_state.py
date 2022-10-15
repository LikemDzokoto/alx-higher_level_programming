#!/usr/bin/python3
''' prints all cities as State_name: (City_id) City_name '''

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                             @localhost:3306/{sys.argv[3]}")

    session = Session(bind=engine)

    for c, s in session.query(City, State).join(State).order_by(City.id):
        print(f"{s.name}: ({c.id}) {c.name}")
