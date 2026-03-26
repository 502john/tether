from fastapi import FastAPI
from fastrtc import Stream, get_tts_model

app = FastAPI()

@app.get("/")
async def root():
        return {"message" : "Hello World"}



