from fastapi import FastAPI
from routes import history_api, login_api, recommend_api
from routes import user_api

app = FastAPI()

# Include API routers
app.include_router(history_api.router, prefix="/api/history", tags=["History"])
app.include_router(recommend_api.router, prefix="/api/recommendation", tags=["Recommendation"])
app.include_router(user_api.router, prefix="/api/user", tags=["User"])
app.include_router(login_api.router, prefix="/api/login", tags=["Login"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Recommendation System API!"}
