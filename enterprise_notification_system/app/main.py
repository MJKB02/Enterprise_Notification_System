from fastapi import FastAPI
from app.routes import auth_routes, otp_routes, notification_routes

app = FastAPI(title="Enterprise Notification System")

app.include_router(auth_routes.router)
app.include_router(otp_routes.router)
app.include_router(notification_routes.router)

@app.get("/")
def home():
    return {"message": "System Running"}