from fastapi import FastAPI
from routes import history, recommend, user

app = FastAPI()

# Include API routers
app.include_router(history.router, prefix="/api/history", tags=["History"])
app.include_router(recommend.router, prefix="/api/recommendation", tags=["Recommendation"])
app.include_router(user.router, prefix="/api/user", tags=["User"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Recommendation System API!"}
