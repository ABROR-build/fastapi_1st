from fastapi import FastAPI
from database import SessionLocal, engine
from schemas import SignUp
from models import User
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/signup/")
async def signup(user: SignUp):
    session = SessionLocal()

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return {'message': 'Username exists'}

    new_user = User(
        username=user.username,
        password=user.password
    )
    session.add(new_user)
    session.commit()
    return {'message': 'User created'}
