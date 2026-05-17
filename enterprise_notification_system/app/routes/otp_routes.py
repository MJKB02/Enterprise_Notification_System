from fastapi import APIRouter

router = APIRouter(prefix="/otp", tags=["OTP"])

@router.post("/send")
def send_otp():
    return {"message": "OTP sent"}

@router.post("/verify")
def verify_otp():
    return {"message": "OTP verified"}