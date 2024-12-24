from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Models
class User(BaseModel):
    id: int
    name: str
    email: str

# Database simulation
users_db = {}

# Routes
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de usuarios"}

@app.post("/users/", response_model=User)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user = users_db.pop(user_id, None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
