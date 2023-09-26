from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./test.db"
Base: DeclarativeMeta = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/")
def register(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "id": new_user.id}


@app.post("/signin/")
def signin(username: str, password: str, db: Session = Depends(get_db)):
    query = text("SELECT * FROM users WHERE username = :username AND password = :password")
    print(query)
    result = db.execute(query, {'username': username, 'password': password}).fetchone()
    if result is None:
        raise HTTPException(status_code=400, detail="Username not found")

    return {"username": result[1], "message": "Signed in successfully"}



