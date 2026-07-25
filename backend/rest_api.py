'''
Implememting Rest API test practice
'''
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI()

users = {}
next_id = 1


class UserCreate(BaseModel):
    '''class'''
    name: str
    email: EmailStr


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    '''create user'''
    global next_id

    if not user.name.strip():
        raise HTTPException(
            status_code=422,
            detail="Name cannot be empty"
        )

    # EmailStr already validates email format
    if any(existing["email"] == user.email for existing in users.values()):
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email,
    }

    users[next_id] = new_user
    next_id += 1

    return new_user
