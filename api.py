from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "SPARK001"

@app.get("/")
def home():
    return {"message": "API is live 🚀"}

@app.get("/chat")
def chat(msg: str, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"response": f"You said: {msg}"}
