from fastapi import FastAPI
from services.llm import get_llm_response
from schemas.chat import ChatResponse, ChatRequest, Message

app = FastAPI()


# Path Operation Decorator
@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    reply = get_llm_response(req.messages)
    return {"response": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)