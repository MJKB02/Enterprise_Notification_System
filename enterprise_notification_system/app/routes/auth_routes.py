from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup():
    return {"message": "Signup successful"}

@router.post("/login")
def login():
    return {"access_token": "jwt-token"}