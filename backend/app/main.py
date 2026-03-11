from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import test


app = FastAPI()
app.include_router(test.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}