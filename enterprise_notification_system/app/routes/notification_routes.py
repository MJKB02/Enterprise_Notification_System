from fastapi import APIRouter

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/send")
def send_notification():
    return {"message": "Notification queued"}