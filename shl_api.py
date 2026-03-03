from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(query: Query):
    return {"query": query.text, "recommendations": ["Example Assessment 1", "Example Assessment 2"]}
